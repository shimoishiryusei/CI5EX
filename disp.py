# -*- coding: utf-8 -*-
from grove_rgb_lcd import *
import time
def set_disp(times):
    Year,Month,Day,Hour,Minute,Second = times
    Time_strings = str(Year)+"/"+str(Month)+"/"+str(Day)+"\n"+str(Hour)+":"+str(Minute)+":"+str(Second)
    while True:
        setText(Time_strings)
        setRGB(0,128,64)
        time.sleep(1)
