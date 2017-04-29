class ActionCardMutationGenerator(object):
    @staticmethod
    def generate(actor_id, api, card, result):
        mutation_template = card.template.mutation_template
        mutation = api.mutations.create_and_register(mutation_template, source_actor_id=actor_id, **result.exports)
        api.actors.transfer_card_to_in_play(
            source_actor_id=actor_id,
            targeted_actor_id=result.exports["targeted_actor_id"],
            card_id=card.id,
            mutation_id=mutation.id)
        return mutation.id