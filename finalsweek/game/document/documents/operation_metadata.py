from game.document.documents.document_base import DocumentBase


class OperationMetadata(DocumentBase):
    _field_definitions = {
        # mediums
        "system":                bool,  # came from system (usually don't F with this...)
        "actor_action":          bool,  # came from an actor action
        "status_effect":         bool,  # came from a status effect
        "automatic_effect":      bool,  # came from an auto-card or some other board state

        # card types
        "card":                  bool,  # came from a card
        "discipline_card":       bool,  # came from a discipline card
        "afterschool_card":      bool,  # came from an afterschool card
        "action_card":           bool,  # a user played an action card to trigger this effect
        "played_card":           bool,  # a user played a card to trigger this effect
        "automatic_card":        bool,  # came from a card, but was not played

        # cost related
        "afterschool_card_cost": bool,  # effect was caused by purchasing AS card
        "card_cost":             bool,  # effect was caused by purchasing any card

        # special
        "proximate_effect":      bool,  # effect was caused by something in a seat
        "on_draw":               bool,  # effect was caused as soon as a card was drawn

        # temporal
        "turn_bound":            bool,  # effect source will be gone after turn
        "phase_bound":           bool,  # effect source will be gone after phase
        "stage_bound":           bool,  # effect source will be gone after stage
        "use_bound":             bool,  # effect source will be gone after use
        "until_removed":         bool,  # effect source will persist until removed
        "permanent":             bool,  # effect source is permanent

        # attributes
        "popularity":            bool,  # affects Popularity
        "grades":                bool,  # affects Grades
        "trouble":               bool,  # affects Trouble
        "torment":               bool,  # affects Torment
    }

    @classmethod
    def default_data(cls):
        return {k: False for k in cls._field_definitions.keys()}

    def __init__(self, base_data=None, parent=None) -> None:
        self.system = False
        self.actor_action = False
        self.status_effect = False
        self.automatic_effect = False
        self.card = False
        self.discipline_card = False
        self.afterschool_card = False
        self.action_card = False
        self.played_card = False
        self.automatic_card = False
        self.afterschool_card_cost = False
        self.card_cost = False
        self.proximate_effect = False
        self.on_draw = False
        self.turn_bound = False
        self.phase_bound = False
        self.stage_bound = False
        self.use_bound = False
        self.until_removed = False
        self.permanent = False
        self.popularity = False
        self.grades = False
        self.trouble = False
        self.torment = False
        super().__init__(base_data or self.default_data(), parent)

    def matches(self, obj) -> bool:
        for k, v in vars(self).items():
            if getattr(obj, k) == v:
                return True
        return False
