# -*- coding: utf-8 -*-
from os import lseek
from grove_rgb_lcd import *
import time
import get_radian

def set_disp(times, THs):
    Deg = get_radian.get_degree()
    Year,Month,Day,Hour,Minute,Second = times
    Tmp = THs[0]
    Hmd = THs[1]
    Time_strings = str(Month)+"/"+str(Day)+" "+str(Hour)+":"+str(Minute)+":"+str(Second) + "\n" + "T:" + str(Tmp) + " " + "H:" + str(Hmd)
    setText(Time_strings)
    if Deg < 500:
        setRGB(248,248,255)
    else:
        setRGB(199,21,133)
    time.sleep(0.5)
