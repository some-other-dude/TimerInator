import datetime as dt
import time
import tkinter as tk
# from graphics import *

import clock as tc

c = tc.Clock(name = "My Clock", total_time = 5, current_time = 5, remaining_time = 5, start_time = dt.datetime.now())


clock_win = tk.Tk()
clock_win.geometry("300x300")

c.status = "running"

clock_label = tk.Label(master = clock_win, text=c.status, height=50, width = 100, bg = 'green')
clock_label.place(relx=0.5, rely=0.5, anchor="center")
clock_win.update()

while c.status == "running":
    if c.current_time > 0:
        clock_label.config(text=c.make_hms())
        clock_win.update()
        time.sleep(1)
        c.tick_clock()
    else:
        clock_label.config(text="DONE")
        clock_win.update()
        time.sleep(2)
        clock_win.update()
        clock_win.destroy()
