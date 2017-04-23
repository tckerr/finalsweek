class OperationMetadataType(object):
    # mediums
    System = "System"  # came from system (usually don't F with this...)
    ActorAction = "ActorAction"  # came from an actor action
    StatusEffect = "StatusEffect"  # came from a status effect
    AutomaticEffect = "StatusEffect"  # came from an auto-card or some other board state

    # card types
    Card = "Card"  # came from a card
    DisciplineCard = "DisciplineCard"  # came from a discipline card
    AfterSchoolCard = "AfterSchoolCard"  # came from an afterschool card
    ActionCard = "ActionCard"  # a user played an action card to trigger this effect
    PlayedCard = "PlayedCard"  # a user played a card to trigger this effect
    AutomaticCard = "AutomaticCard"  # came from a card, but was not played

    # cost related
    AfterSchoolCardCost = "AfterSchoolCardCost"  # effect was caused by purchasing AS card
    CardCost = "CardCost"  # effect was caused by purchasing any card

    # special
    ProximateEffect = "ProximateEffect"  # effect was caused by something in a seat
    OnDraw = "OnDraw"  # effect was caused as soon as a card was drawn

    # temporal
    TurnBound = "TurnBound"  # effect source will be gone after turn
    PhaseBound = "PhaseBound"  # effect source will be gone after phase
    StageBound = "StageBound"  # effect source will be gone after stage
    UseBound = "UseBound"  # effect source will be gone after use
    UntilRemoved = "UntilRemoved"  # effect source will persist until removed
    Permanent = "Permanent"  # effect source is permanent

    # attributes
    Popularity = "Popularity"  # affects Popularity
    Grades = "Grades"  # affects Grades
    Trouble = "Trouble"  # affects Trouble
    Torment = "Torment"  # affects Torment


class OperationMetadata(object):
    def __init__(self) -> None:
        super().__init__()
        self.System = False
        self.ActorAction = False
        self.StatusEffect = False
        self.AutomaticEffect = False
        self.Card = False
        self.DisciplineCard = False
        self.AfterSchoolCard = False
        self.ActionCard = False
        self.PlayedCard = False
        self.AutomaticCard = False
        self.AfterSchoolCardCost = False
        self.CardCost = False
        self.ProximateEffect = False
        self.OnDraw = False
        self.TurnBound = False
        self.PhaseBound = False
        self.StageBound = False
        self.OnDraw = False
        self.UseBound = False
        self.Permanent = False
        self.Permanent = False
