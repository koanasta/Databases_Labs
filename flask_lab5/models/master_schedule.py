class MastersSchedule:
    def __init__(self, idschedule, master_id, work_date, start_time, end_time):
        self.idschedule = idschedule
        self.master_id = master_id
        self.work_date = work_date
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {
            "idschedule": self.idschedule,
            "master_id": self.master_id,
            "work_date": self.work_date,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
