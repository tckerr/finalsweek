class MutationMatcher(object):
    def matches(self, mutation, operation):
        if not self._matches_on_targeted_actor(mutation, operation):
            return False
        if mutation.match_all:
            return self._all_match(mutation.tags, operation)
        return self._any_matches(mutation.tags, operation)

    @staticmethod
    def _matches_on_targeted_actor(mutation, operation):
        return mutation.targeted_actor_id is None \
               or operation.targeted_actor_id == mutation.targeted_actor_id

    @staticmethod
    def _any_matches(tags, operation):
        for tag in tags:
            if tag in operation.tags:
                return True
        return False

    @staticmethod
    def _all_match(tags, operation):
        for tag in tags:
            if tag not in operation.tags:
                return False
        return True
