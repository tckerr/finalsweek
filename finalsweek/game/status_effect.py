class AttributeModifier(object):
    def __init__(self, attribute_id, criteria):
        self.attribute_id = attribute_id
        self.criteria = criteria

    # override me
    @staticmethod
    def modify(val):
        return val


class StatusEffect(object):

    def __init__(self, attribute_modifiers):
        self.attribute_modifiers = {}
        for mod in attribute_modifiers:
            self.attribute_modifiers[mod.attribute_id] = mod

    def apply_attribute_modifier(self, attribute_id, val, criteria):
        if attribute_id in self.attribute_modifiers:
            modifier = self.attribute_modifiers.get(attribute_id)
            # Does the modifier apply at this time?
            if modifier.criteria == criteria:
                # Apply multiplicative modifier
                return modifier.modify(val)
        return val

    def filter_target_eligiblity(self, target, targeting_criteria): pass

    def generate_action(self, turn_type): pass

    # call each turn?
    def expire_if_complete(self): pass