# services/masters_schedule_service.py
from dao.masters_schedule_dao import MastersScheduleDAO
from models.master_schedule import MastersSchedule

class MastersScheduleService:

    def __init__(self):
        self.dao = MastersScheduleDAO()

    def list_all(self):
        return self.dao.get_all()

    def get(self, id):
        return self.dao.get_by_id(id)

    def create(self, data):
        ms = MastersSchedule(
            masters_id=data.get("masters_id"),
            work_date=data.get("work_date"),
            shift=data.get("shift")
        )
        return self.dao.create(ms)

    def update(self, id, data):
        ms = MastersSchedule(
            masters_id=data.get("masters_id"),
            work_date=data.get("work_date"),
            shift=data.get("shift")
        )
        return self.dao.update(id, ms)

    def delete(self, id):
        return self.dao.delete(id)
