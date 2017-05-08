from game.gameflow.actions.base import ActionBase
from trace.logger import Logger


class ScoreAction(ActionBase):
    def execute(self, actor_id, api):
        super().execute(actor_id, api)
        actor = api.actors.get(actor_id)
        template = " -> Score for actor {actor_name} ({actor_id}): {score} (Grades: {grades}, Popularity: {popularity})"
        Logger.log(template.format(
            actor_name=actor.name,
            actor_id=actor_id,
            score=actor.grades + actor.popularity,
            grades=actor.grades,
            popularity=actor.popularity))
