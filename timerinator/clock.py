import datetime as dt
import multiprocessing

class Clock:

    def __init__(self,
                name = "New Clock",
                total_time = 0,
                current_time = 0,
                remaining_time = 0,
                start_time = None,
                status = "stopped",
                pid = None):

        self.name = name
        self.total_time = total_time
        self.current_time = current_time
        self.remaining_time = remaining_time
        self.start_time = start_time
        self.status = status
        self.pid = pid

    def update_remaining_time(self):
        if self.current_time > 0:
            self.remaining_time = self.current_time
        else:
            self.remaining_time = 0

    def projected_end_time(self):
        p_e_t = dt.datetime.now() + dt.timedelta(seconds = self.remaining_time)
        return p_e_t

    def tick_clock(self):
        now = dt.datetime.now()
        self.current_time = int((now - self.start_time).total_seconds())
        self.update_remaining_time()
