from configuration.models import StudentInfo


class StudentInfoAdapter(object):
    @staticmethod
    def adapt(data):
        return {
            "id":               str(data.id),
            "first_name":       data.first_name,
            "last_name":        data.last_name,
            "backstory":        data.backstory,
            "perk_name":        data.perk_name,
            "perk_description": data.perk_description,
            "fear_name":        data.fear_name,
            "fear_description": data.fear_description
        }


class StudentInfoFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.student_info_adapter = StudentInfoAdapter()

    def create(self):
        default_student_info = list(StudentInfo.objects.order_by("id").all())
        return [self.student_info_adapter.adapt(card) for card in default_student_info]
