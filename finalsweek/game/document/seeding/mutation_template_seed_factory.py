from game.document.seeding.operation_modifier_seed_factory import OperationModifierSeedFactory
from game.models import MutationTemplate


class MutationTemplateAdapter(object):
    def __init__(self):
        self.operation_modifier_seed_factory = OperationModifierSeedFactory()

    def adapt(self, data):
        return {
            "id":                 str(data.id),
            "tags":               data.tags,
            "priority":           data.priority,
            "match_all":          data.match_all,
            "expiry_criteria":    data.expiry_criteria,
            "uses":               data.uses,
            "operation_modifier": self.operation_modifier_seed_factory.create(data.operation_modifier)
        }


class MutationTemplateSeedFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.mutation_template_adapter = MutationTemplateAdapter()

    def create(self):
        loaded = list(MutationTemplate.objects.prefetch_related("operation_modifier").all())
        operation_modifiers = {}
        for mutation_effect in loaded:
            adapted = self.mutation_template_adapter.adapt(mutation_effect)
            operation_modifiers[adapted["id"]] = adapted
        return operation_modifiers
