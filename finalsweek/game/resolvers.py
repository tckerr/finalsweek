from game.actions import DrawAction
from game.settings import settings
from game.models import PileCard
from django.db import models

class AutomaticActionResolver(object):

    def resolve(self, turn):
        if turn.phase.phase_type_id == "Accumulation":
            cards_needed = settings["hand_size"] - PileCard.objects.filter(pile=turn.actor.action_hand).count()
            effective_draw = cards_needed if cards_needed > 0 else 0
            return DrawAction(effective_draw, turn.actor, "Action")


def increase(values, field, amount):
    real_amount = amount[0]
    old_value = getattr(values, field)
    new_value = max(0, old_value + int(real_amount))
    print("         --> Updating {} on {} from {} by {} to {}. (received: {})".format(field, values, str(old_value), str(real_amount), str(new_value), amount))
    setattr(values, field, new_value)
    if issubclass(values.__class__, models.Model):
        values.save()

def decrease(values, field, amount):
    return increase(values, field, [int(amount[0])*-1])

def set_prop(values, field, amount):
    real_amount = amount[0]
    old_value = getattr(values, field)
    new_value = max(0, int(real_amount))
    print("         --> Updating {} on {} from {} to {}. (received: {})".format(field, values, str(old_value), str(real_amount), str(new_value), amount))
    setattr(values, field, new_value)
    if issubclass(values.__class__, models.Model):
        values.save()

class OperatorResolver(object):

    operators = {
        "increase": increase,
        "decrease": decrease,
        "set": set_prop
    }

    def resolve(self, operator_id):
        result = self.operators.get(operator_id, False)
        if not result:
            raise Exception("Unknown operator {}".format(operator_id))
        return result

        
