from util.random import random_id, shuffle


class ActionCardDeckSeedFactory(object):
    @staticmethod
    def create(templates, settings):
        template_list = sorted(templates.values(), key=lambda t: t["id"])
        filtered_templates = list(filter(lambda c: c["card_type"] == "Action", template_list))
        total_cards = settings["total_cards"]
        cards_per_type = int(total_cards / len(filtered_templates))
        card_list = []
        for template in filtered_templates:
            for _ in range(0, cards_per_type):
                card_list.append({
                    "id":                       random_id(),
                    "card_template_id": template["id"]
                })
        shuffle(card_list)
        return {
            "id":    random_id(),
            "cards": card_list
        }
