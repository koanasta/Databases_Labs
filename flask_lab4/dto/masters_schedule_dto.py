# dto/masters_schedule_dto.py
class MastersScheduleDTO:
    def __init__(self, idmasters_schedule, masters_id, work_date, shift):
        self.idmasters_schedule = idmasters_schedule
        self.masters_id = masters_id
        self.work_date = work_date
        self.shift = shift

    @staticmethod
    def from_model(m):
        d = m.to_dict()
        return MastersScheduleDTO(
            d["idmasters_schedule"],
            d["masters_id"],
            d["work_date"],
            d["shift"]
        )

    def to_dict(self):
        return {
            "idmasters_schedule": self.idmasters_schedule,
            "masters_id": self.masters_id,
            "work_date": self.work_date,
            "shift": self.shift
        }
