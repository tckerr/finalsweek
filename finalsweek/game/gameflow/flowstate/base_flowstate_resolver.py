class BaseFlowstateResolver(object):
    @staticmethod
    def _filter_related_manager_itemset(itemset, comp_val, attr_key, set_number=0):
        filtered_items = list(filter(lambda x: getattr(x, attr_key) == comp_val, itemset.all()))
        if len(filtered_items) < set_number + 1:
            return None
        return filtered_items[set_number]

    @staticmethod
    def _complete_stage(stage, api):
        api.stages.complete_stage(stage.id)

    @staticmethod
    def _complete_phase(phase, api):
        api.phases.complete_phase(phase.id)