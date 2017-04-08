from game.models import Stage, Phase, Turn
from django.utils import timezone

class Reset(Exception): pass

class PhaseFilter(object):
    filter_types = ("Accumulation", "Classtime", "Dismissal", "After School", "Score", "Choose Seats",)

    def get_phase_counts_for_stage(self, stage):
        phases = list(stage.phases.filter(completed__isnull=False))
        return { pt: self.__get_len_by_phase_type_id(phases, pt) for pt in self.filter_types }

    def __get_len_by_phase_type_id(self, phases, phase_type_id):
        filtered = filter(lambda p: p.phase_type_id == phase_type_id, phases)
        return len(list(filtered))

class StageGenerator(object):

    def __init__(self):
        self.phase_filter = PhaseFilter()

    def get_or_generate(self, game):
        pending = game.stages.filter(completed__isnull=True)
        if pending.count() > 1:
            raise Exception("More than 1 active stage")
        if pending.count() == 1:
            stage = pending.first()
            if not self.__complete_if_needed(stage):
                return stage
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
        completed = self.__get_completed_stages(game)
        gamestart = self.__extract_stage_by_type(completed, "GameStart")
        if not gamestart:
            return "GameStart"
        play = self.__extract_stage_by_type(completed, "Play")
        if not play:
            return "Play"
        scoring = self.__extract_stage_by_type(completed, "Scoring")
        if not scoring:
            return "Scoring"

    def __get_completed_stages(self, game):
        completed_stages = list(game.stages.filter(completed__isnull=False))
        return completed_stages
            
    def __extract_stage_by_type(self, stages, stage_type_id):
        filtered_stages = list(filter(lambda s: s.stage_type_id == stage_type_id, stages))
        return filtered_stages[0] if filtered_stages else None

    def __complete_if_needed(self, stage):
        phase_counts = self.phase_filter.get_phase_counts_for_stage(stage)
        if stage.stage_type_id == "GameStart":
            return self.__complete_gamestart_if_needed(stage, phase_counts)
        elif stage.stage_type_id == "Scoring":
            return self.__complete_scoring_if_needed(stage, phase_counts)
        elif stage.stage_type_id == "Play":
            return self.__complete_play_if_needed(stage, phase_counts)
        raise Exception("Unknown stage type {}".filter.stage.stage_type_id)

    def __complete_gamestart_if_needed(self, stage, phase_counts):
        if phase_counts.get("Choose Seats", 0) > 0:
            self.__complete_stage(stage)
            return True
        return False

    def __complete_scoring_if_needed(self, stage, phase_counts):
        if phase_counts.get("Score", 0) > 0:
            self.__complete_stage(stage)
            return True
        return False

    def __complete_play_if_needed(self, stage, phase_counts):
        max_phases = stage.game.play_phase_count
        relevant_items = { k: phase_counts[k] for k in ("Accumulation", "Classtime", "Dismissal", "After School", ) }
        if all([v == max_phases for k, v in relevant_items.items()]):
            self.__complete_stage(stage)
            return True
        return False

    def __complete_stage(self, stage):
        stage.completed = timezone.now()
        stage.save()

class PhaseGenerator(object):

    def __init__(self):
        self.phase_filter = PhaseFilter()

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
            return "Choose Seats"
        elif stage.stage_type_id == "Scoring":
            return "Score"
        elif stage.stage_type_id == "Play":
            counts = self.phase_filter.get_phase_counts_for_stage(stage)
            max_phases = stage.game.play_phase_count
            for current in range(1, max_phases+1):
                for phase_type in ("Accumulation", "Classtime", "Dismissal", "After School", ):
                    if counts[phase_type] < current:
                        return phase_type
        raise Exception("Shouldn't get here")


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