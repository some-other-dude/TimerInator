import datetime as dt
import time

import clock as tc

c = tc.Clock(name = "My Clock", total_time = 10, current_time = 10, remaining_time = 10, start_time = dt.datetime.now())

while c.current_time > -3:
    c.tick_clock()
    c.debug_info()
    time.sleep(1)
