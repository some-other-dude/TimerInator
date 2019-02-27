import datetime
import multiprocessing

class Clock:

    def __init__(self, name = "New Clock", total_time = 0, current_time = 0, remaining_time = 0, status = "stopped", pid = None):
        self.name = name
        self.total_time = total_time
        self.current_time = current_time
        self.remaining_time = remaining_time
        self.status = status
        self.pid = pid
