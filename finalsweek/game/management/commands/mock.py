from django.core.management.base import BaseCommand
#
from game.interface.routers import GameRouter
from game.interface.actions import UseActionCardAction
from random import choice

player_count = 4
router = GameRouter()

class Command(BaseCommand):

    def handle(self, *args, **options):
        game_info = router.create(player_count)
        actors = [a for a in game_info.actors]

        while True:
            summary = router.load(actors[0].id)
            if summary.complete:
                break
            current_actor_id = summary.current_turn_actor_id
            options = router.get_turn_options(current_actor_id)
            print("\n-----+ NEW TURN +-----")
            print("Actor {}, phase type: {}".format(current_actor_id, options.phase_type))
            if options.phase_type == "Classtime":
                print("Action cards:", [c[1].name for c in options.action_cards])
                random_choice = choice([pc_id for pc_id, card in options.action_cards])
                action = UseActionCardAction(current_actor_id, random_choice, {})
                keep_going = True

                while keep_going:
                    prompt_digest = router.take_turn(current_actor_id, action)
                    if not prompt_digest:
                        break
                    prompt = prompt_digest.prompt
                    for answer_key, prompt_options in prompt.pending:
                        print("Options:")
                        for option in prompt_options:
                            print("   - {}: {}".format(option["display"], option["id"]))
                        #selection = input()
                        if not prompt_options:
                            print("Skipping card", random_choice, "... no options")
                            keep_going = False
                            break
                        selection = choice([o["id"] for o in prompt_options])
                        prompt.answer(answer_key, selection)
                        action.decisions = prompt.cumulative_answers

            else:
                router.take_turn(current_actor_id, None)

        print("Game over!")

