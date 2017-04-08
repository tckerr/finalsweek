from game.models import Stage, Phase, Turn
from django.utils import timezone

class Reset(Exception): pass

class StageGenerator(object):

    def get_or_generate(self, game):
        pending = game.stages.filter(completed__isnull=True)
        if pending.count() == 1:
            return pending.first()
        elif pending.count() > 1:
            raise Exception("More than 1 active stage")
        return self.__create(game)

    def __create(self, game):
        stage_type_id = self.__resolve_upcoming_stage_type(game)
        if stage_type_id is None:
            return
        stage = Stage()
        stage.game = game
        stage.stage_type_id = stage_type_id
        stage.save()
        return stage

    def __resolve_upcoming_stage_type(self, game):
        if not game.stages.filter(completed__isnull=False, stage_type_id="GameStart").count() > 0:
            return "GameStart"
        elif not game.stages.filter(completed__isnull=False, stage_type_id="Play").count() > 0:
            return "Play"
        elif not game.stages.filter(completed__isnull=False, stage_type_id="Scoring").count() > 0:
            return "Scoring"

class PhaseGenerator(object):

    def get_or_generate(self, stage):
        pending = stage.phases.filter(completed__isnull=True)
        if pending.count() == 1:
            return pending.first()
        elif pending.count() > 1:
            raise Exception("More than 1 active phase")
        return self.__create(stage)

    def __create(self, stage):
        phase = Phase()
        phase.stage = stage
        phase.phase_type_id = self.__resolve_upcoming_phase_type(stage)
        phase.save()
        assert phase.phase_type.stage_type == phase.stage.stage_type
        return phase

    def __resolve_upcoming_phase_type(self, stage):
        if stage.stage_type_id == "GameStart":
            completed_seats = stage.phases.filter(completed__isnull=False, phase_type_id="Choose Seats").count()
            if completed_seats > 0:
                self.__complete_stage(stage)
            return "Choose Seats"
        elif stage.stage_type_id == "Scoring":
            completed_scores = stage.phases.filter(completed__isnull=False, phase_type_id="Score").count()
            if completed_scores > 0:
                self.__complete_stage(stage)
            return "Score"
        elif stage.stage_type_id == "Play": 
            completed_accumulation = stage.phases.filter(completed__isnull=False, phase_type_id="Accumulation").count()
            completed_classtime = stage.phases.filter(completed__isnull=False, phase_type_id="Classtime").count()
            completed_dismissal = stage.phases.filter(completed__isnull=False, phase_type_id="Dismissal").count()
            completed_afterschool = stage.phases.filter(completed__isnull=False, phase_type_id="After School").count()
            max_phases = stage.game.play_phase_count
            if all([x == max_phases for x in (completed_accumulation, completed_classtime, completed_dismissal, completed_afterschool)]):
                self.__complete_stage(stage)
            else:
                for current in range(1, max_phases+1):
                    if completed_accumulation < current:
                        return "Accumulation"
                    if completed_classtime < current:
                        return "Classtime"
                    if completed_dismissal < current:
                        return "Dismissal"
                    if completed_afterschool < current:
                        return "After School"

    def __complete_stage(self, stage):
        stage.completed = timezone.now()
        stage.save()
        raise Reset()

class TurnGenerator(object):

    def get_or_generate(self, phase):
        pending = phase.turns.filter(completed__isnull=True)
        if pending.count() > 0:
            return pending.first()
        elif pending.count() > 1:
            raise Exception("More than 1 active turn")
        return self.__create(phase)

    def __create(self, phase):
        turn = Turn()
        turn.phase = phase
        turn.actor = self.__resolve_upcoming_actor(phase)
        turn.save()
        return turn

    def __resolve_upcoming_actor(self, phase):
        actors = phase.stage.game.actors.order_by("id")
        if not actors.count() > 2:
            raise Exception("You must have at least 2 actors in a game.")
        turns = phase.turns.filter(completed__isnull=False)
        turn_count = self.__get_turn_count(phase)
        for actor in actors:
            actor_turns = filter(lambda turn: turn.actor == actor, turns)
            if len(list(actor_turns)) < turn_count:
                return actor
        phase.completed = timezone.now()
        phase.save()
        raise Reset()

    def __get_turn_count(self, phase):
        return 2 if phase.phase_type_id == "Classtime" else 1