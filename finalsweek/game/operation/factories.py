from game.document.documents.mutation import Mutation
from game.exceptions import ExportException
from util import guid


class MutationFactory(object):
    _valid_exports = ('targeted_actor_id', 'source_actor_id')

    @classmethod
    def create_from_template(cls, template, **exports):
        cls._validate_exports(exports)
        mutation_data = {
            "id":                 guid(),
            "tags":               template.tags,
            "priority":           template.priority,
            "match_all":          template.match_all,
            "expiry_criteria":    template.expiry_criteria,
            "operation_modifier": template.operation_modifier
        }
        mutation_data.update(exports)
        mutation = Mutation(mutation_data)
        return mutation

    @classmethod
    def _validate_exports(cls, exports):
        for k in exports.keys():
            if k not in cls._valid_exports:
                message = "Export {} is not valid for a mutation effect.".format(k)
                raise ExportException(message)