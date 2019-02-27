import datetime as dt
import time
# import tkinter as tk
from graphics import *

import clock as tc

# c = tc.Clock(name = "My Clock", total_time = 10, current_time = 10, remaining_time = 10, start_time = dt.datetime.now())
#
# while c.current_time > -3:
#     c.tick_clock()
#     print(c.make_hms())
#     time.sleep(1)


win = GraphWin()

c = tc.Clock(name = "My Clock", total_time = 10, current_time = 10, remaining_time = 10, start_time = dt.datetime.now())

while c.current_time > -3:
    c.tick_clock()
    tl = Point(win.width/2 - 50,10)
    br = Point(win.width/2 + 50,50)
    rect = Rectangle(tl, br)
    rect.setFill('white')
    rect.draw(win)
    message = Text(Point(win.getWidth()/2, 20), c.make_hms())
    message.draw(win)
    time.sleep(1)

message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()
