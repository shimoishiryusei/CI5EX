# -*- coding: utf-8 -*-
from os import lseek
from grove_rgb_lcd import *
import time
def set_disp(times, THs):
    Year,Month,Day,Hour,Minute,Second = times
    Tmp = THs[0]
    Hmd = THs[1]
    Time_strings = str(Month)+"/"+str(Day)+" "+str(Hour)+":"+str(Minute)+":"+str(Second) + "\n" + "T:" + str(Tmp) + " " + "H:" + str(Hmd)
    setText(Time_strings)
    setRGB(0,128,64)
    time.sleep(0.5)
