from game.definitions import CardTypeName
from util.random import random_id, shuffle


class DisciplineCardDeckSeedFactory(object):

    def create(self, templates, settings):
        cards = self._create_cards(templates, settings)
        return {
            "id":    random_id(),
            "cards": cards
        }

    # TODO: remove duplication between this and action card factory
    @staticmethod
    def _create_cards(templates, settings):
        template_list = sorted(templates.values(), key=lambda t: t["id"])
        filtered_templates = list(filter(lambda c: c["card_type"] == CardTypeName.DisciplineCard, template_list))
        total_cards = settings["discipline_card_deck_size"]
        cards_per_type = int(total_cards / len(filtered_templates))
        card_list = []
        for template in filtered_templates:
            for _ in range(0, cards_per_type):
                card_list.append({
                    "id":               random_id(),
                    "card_template_id": template["id"]
                })
        shuffle(card_list)
        return card_list

