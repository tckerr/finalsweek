from django.utils import timezone

class BaseFlowstateResolver(object):

    def _filter_related_manager_itemset(self, itemset, comp_val, attrkey, set_number=0):
        filtered_items = list(filter(lambda x: getattr(x, attrkey) == comp_val, itemset.all()))
        if len(filtered_items) < set_number + 1:
            return None
        return filtered_items[set_number]

    def _complete(self, mdl):
        if mdl:
            mdl.completed = timezone.now()
            mdl.save()