import datetime as dt
import time
import tkinter as tk
# from graphics import *

import clock as tc

c = tc.Clock(name = "My Clock", total_time = 10, current_time = 10, remaining_time = 10, start_time = dt.datetime.now())
#
# def run_clock(stop_time = 0):
#     while c.current_time <= stop_time:
#         c.tick_clock()
#         print(c.make_hms())
#         time.sleep(1)


# win = GraphWin()
#
# c = tc.Clock(name = "My Clock", total_time = 10, current_time = 10, remaining_time = 10, start_time = dt.datetime.now())
#
# while c.current_time > -3:
#     c.tick_clock()
#     tl = Point(win.width/2 - 50,10)
#     br = Point(win.width/2 + 50,50)
#     rect = Rectangle(tl, br)
#     rect.setFill('white')
#     rect.draw(win)
#     message = Text(Point(win.getWidth()/2, 20), c.make_hms())
#     message.draw(win)
#     time.sleep(1)
#
# message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
# message.draw(win)
# win.getMouse()
# win.close()

# labelText = Stringvar()
# depositLabel = Label(self, textvariable=labelText)
# depositLabel.grid()

# def updateDepositLabel(txt) # you may have to use *args in some cases
#     labelText.set(txt)

clock_win = tk.Tk()
clock_win.geometry("300x300")

c.status = "running"

clock_label = tk.Label(text=c.status)
clock_label.place(relx=0.5, rely=0.5, anchor="center")
clock_win.update()

while c.status == "running":
    if c.current_time > -3:
        clock_label.config(text=c.make_hms())
        clock_win.update()
        time.sleep(1)
        c.tick_clock()
    else:
        clock_label.config(text="DONE")
        clock_win.update()
        time.sleep(2)


# clock_win = tk.Tk()
# c.status = "running"
# lbl = tk.Label(clock_win, textvariable=c.status)
# lbl.grid()
# while c.status == "running":
#     if c.current_time > -3:
#         c.tick_clock()
#         lbl.set(c.make_hms())
#         lbl.grid()
#         clock_win.update()
#         time.sleep(1)
#     else:
#         c.status = "done"
#         # lbl = tk.Label(clock_win, text=c.status)
#         # lbl.pack()
#         clock_win.update()
