# -*- coding: utf-8 -*-
from grove_rgb_lcd import *

def set_disp(times):
    Year,Month,Day,Hour,Minute,Second = times
    while True:
        setText(Year+"年"+Month+"月"+Day+"日"+Hour+"時"+Minute+"分"+Second+"秒")
        setRGB(0,128,64)
