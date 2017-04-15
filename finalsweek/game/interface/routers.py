from game.summaries.builders import GameSummaryBuilder
from game.gameflow.runner import GameRunner

class Perspective(object):
    def __init__(self, actor_id):
        self.actor_id = actor_id

class GameRouter(object):

    def __init__(self):
        self.game_summary_builder = GameSummaryBuilder()
        self.game_runner = GameRunner()
        self.digest_provider = DigestProvider()

    def create(self, player_count):
        game = self.game_runner.create(player_count)
        current_turn = self.game_runner.get_current_turn(game)
        return self.__build_summary(game, current_turn, None)
    
    def load(self, actor_id):
        game = self.game_runner.load(actor_id)  
        current_turn = self.game_runner.get_current_turn(game)    
        summary = self.__build_summary(game, current_turn, actor_id)  
        return summary  

    def take_turn(self, actor_id, action):
        # TODO: dont hardcode UseActionCardAction
        turn_result = self.game_runner.take_turn(actor_id, action)  
        game_result = self.load(actor_id)
        return PromptDigest(turn_result, game_result) if turn_result else None

    def __build_summary(self, game, current_turn, actor_id=None):
        return self.game_summary_builder.build(game, current_turn, perspective=Perspective(actor_id))

    def get_turn_options(self, actor_id):
        game = self.game_runner.load(actor_id)
        current_turn = self.game_runner.get_current_turn(game)
        return self.digest_provider.provide(actor_id, current_turn)


class Digest(object):

    def __init__(self, turn_active, phase_type):
        self.turn_active = turn_active
        self.phase_type = phase_type

class PromptDigest(Digest):

    def __init__(self, prompt, game_summary):
        self.prompt = prompt
        return super(PromptDigest, self).__init__(True, game_summary.phase)

class NotYourTurnDigest(Digest):
    def __init__(self, phase_type):
        super(NotYourTurnDigest, self).__init__(False, phase_type)


class ClasstimeDigest(Digest):
    def __init__(self):
        self.action_cards = []
        super(ClasstimeDigest, self).__init__(True, "Classtime")

class ClasstimeDigestBuilder(object):
    def __init__(self):
        self.pending_fields = {}

    def with_action_cards(self, action_cards):
        self.pending_fields["action_cards"] = action_cards
        return self

    def build(self):
        digest = ClasstimeDigest()
        for k, v in self.pending_fields.items():
            setattr(digest, k, v)
        return digest

class DigestProvider(object):

    def provide(self, actor_id, current_turn):
        phase_type = current_turn.phase.phase_type_id

        if current_turn.actor_id != actor_id:
            return NotYourTurnDigest(phase_type)

        if not current_turn.phase.phase_type_id == "Classtime":
            return Digest(True, phase_type)

        # for now Classtime is the only one we really care about
        action_hand = current_turn.actor.action_hand
        cards = [(pc.id, pc.card) for pc in action_hand.pile_cards.all()] # TODO: make a class
        return ClasstimeDigestBuilder()\
                    .with_action_cards(cards) \
                    .build()
