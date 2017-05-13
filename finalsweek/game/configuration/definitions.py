from util.listable_class import ListableClass


class StageTypeName:
    GameStart = "Game Start"
    Play = "Play"
    Scoring = "Scoring"


class PhaseTypeName:
    ChooseSeats = "Choose Seats"
    Accumulation = "Accumulation"
    Classtime = "Class Time"
    Dismissal = "Dismissal"
    AfterSchool = "After School"
    Score = "Score"


class CardTypeName:
    ActionCard = "Action Card"
    DisciplineCard = "Discipline Card"
    AfterSchoolCard = "After School Card"


class MutationGameflowBinding(ListableClass):
    Turn = "Turn"  # effect source will be gone after current turn
    NextChooseSeatsPhase = "Next Choose Seats Phase"
    NextAccumulationPhase = "Next Accumulation Phase"
    NextClasstimePhase = "Next Classtime Phase"
    NextDismissalPhase = "Next Dismissal Phase"
    NextAfterSchoolPhase = "Next After School Phase"
    NextScorePhase = "Next Score Phase"
    Phase = "Phase"  # effect source will be gone after current phase
    Stage = "Stage"  # effect source will be gone after current stage
    Game = "Game"  # effect source is permanent


class GameflowTypeMutationGameflowBindingMap(object):
    @staticmethod
    def get(item):
        return GameflowTypeMutationGameflowBindingMap._map.get(item)

    _map = {
        PhaseTypeName.ChooseSeats:  MutationGameflowBinding.NextChooseSeatsPhase,
        PhaseTypeName.Accumulation: MutationGameflowBinding.NextAccumulationPhase,
        PhaseTypeName.Classtime:    MutationGameflowBinding.NextClasstimePhase,
        PhaseTypeName.Dismissal:    MutationGameflowBinding.NextDismissalPhase,
        PhaseTypeName.AfterSchool:  MutationGameflowBinding.NextAfterSchoolPhase,
        PhaseTypeName.Score:        MutationGameflowBinding.NextScorePhase
    }


class Tag(ListableClass):
    System = "System"  # came from system (usually don't F with this...)
    ActorAction = "Actor Action"  # came from an actor action
    StatusEffect = "Status Effect"  # came from a status effect
    AutomaticEffect = "Automatic Effect"  # came from an auto-card or some other board state

    # card types
    Card = "Card"  # came from a card
    DisciplineCard = "Discipline Card"  # came from a discipline card
    AfterSchoolCard = "After School Card"  # came from an afterschool card
    ActionCard = "Action Card"  # a user played an action card to trigger this effect
    PlayedCard = "Played Card"  # a user played a card to trigger this effect
    AutomaticCard = "Automatic Card"  # came from a card, but was not played

    # game logic
    GradesPerTurn = "Grades per Turn"
    TroublePerTurn = "Trouble per Turn"

    # cost related
    AfterSchoolCardCost = "After School Card Cost"  # effect was caused by purchasing AS card
    ActionCardCost = "Action Card Cost"  # effect was caused by purchasing AS card
    CardCost = "Card Cost"  # effect was caused by purchasing any card

    # special
    ProximateEffect = "Proximate Effect"  # effect was caused by something in a seat
    Draw = "Draw"  # effect was caused as soon as a card was drawn
    DrawActionCard = "Draw Action Card"
    DrawAfterSchoolCard = "Draw After School Card"

    # temporal
    TurnBound = "Turn Bound"  # effect source will be gone after turn
    PhaseBound = "Phase Bound"  # effect source will be gone after phase
    StageBound = "Stage Bound"  # effect source will be gone after stage
    UseBound = "Use Bound"  # effect source will be gone after use
    UntilRemoved = "Until Removed"  # effect source will persist until removed
    Permanent = "Permanent"  # effect source is permanent

    # attributes
    Popularity = "Popularity"  # affects Popularity
    Grades = "Grades"  # affects Grades
    Trouble = "Trouble"  # affects Trouble
    Torment = "Torment"  # affects Torment
    Seat = "Seat"


class OperationType(object):
    # mod types
    Draw = "Draw"
    DefineEligibility = "DefineEligibility"  # target is being selected for something
    ModifyAttribute = "ModifyAttribute"  # target has already been selected and is getting some change
    ExtractInfo = "ExtractInfo"  # target is being selected for non-public info
    ModifySeat = "ModifyRelationship"


class OperatorType(object):
    Add = "Add"
    Set = "Set"
    Get = "Get"
    RefillActionCardHand = "RefillActionCardHand"
