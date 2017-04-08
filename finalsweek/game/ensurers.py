from game.models import StageType, PhaseType, StudentInfo, CardType, Card

class GameCreationEnsurer(object):
    def __init__(self):
        self.type_ensurer = TypeEnsurer()
        self.student_info_ensurer = StudentInfoEnsurer()
        self.card_type_ensurer = CardTypeEnsurer()
        self.card_ensurer = CardEnsurer()

    def ensure(self):
        self.student_info_ensurer.ensure()
        self.type_ensurer.ensure() 
        self.card_type_ensurer.ensure() 
        self.card_ensurer.ensure() 

class TypeEnsurer(object):
    def ensure(self):
        for stage_type in ("GameStart", "Play", "Scoring"):
            self.__ensure_stage_type(stage_type)
        for parent_stage_type, phase_type, auto in (
                ("GameStart", "Choose Seats", False),
                ("Play", "Accumulation", True),
                ("Play", "Classtime", False),
                ("Play", "Dismissal", False),
                ("Play", "After School", False),
                ("Scoring", "Score", True)):
            self.__ensure_phase_type(parent_stage_type, phase_type, auto)

    def __ensure_stage_type(self, stage_type):
        if not StageType.objects.filter(id=stage_type):
            model_object = StageType()
            model_object.id = stage_type
            model_object.save()

    def __ensure_phase_type(self, parent_stage_type, phase_type, auto):
        if not PhaseType.objects.filter(id=phase_type, stage_type_id=parent_stage_type, is_automatic=auto):
            model_object = PhaseType()
            model_object.id = phase_type
            model_object.is_automatic = auto
            model_object.stage_type_id = parent_stage_type
            model_object.save()

class StudentInfoEnsurer(object):
    def ensure(self):
        if not StudentInfo.objects.filter(name="Test Student").count() > 0:
            student_info = StudentInfo()
            student_info.name = "Test Student"
            student_info.backstory = "Just a simple tester."
            student_info.save()

class CardTypeEnsurer(object):
    types = ("AfterSchool", "Discipline", "Action",)
    def ensure(self):
        for type in self.types:
            if not CardType.objects.filter(id=type):
                card_type = CardType()
                card_type.id = type
                card_type.save()

class CardEnsurer(object):
    names = ("Joke", "Torment", "Pay Attention",)
    def ensure(self):
        return
        for name in self.names:
            if not Card.objects.filter(name=name):
                card = Card()
                card.card_type_id = "Action"
                card.name = name
                card.targeting_sift = '{"nothing":"atall"}'
                card.save()