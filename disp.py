# -*- coding: utf-8 -*-
from grove_rgb_lcd import *
import time
def set_disp(times):
    Year,Month,Day,Hour,Minute,Second = times
    Time_strings = str(Year)+"年"+str(Month)+"月"+str(Day)+"日"+str(Hour)+"時"+str(Minute)+"分"+str(Second)+"秒"
    while True:
        setText(Time_strings)
        setRGB(0,128,64)
        time.sleep(1)
