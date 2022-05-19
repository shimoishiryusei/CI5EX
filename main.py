# -*- coding: utf-8 -*-
import alarm
import get_TH
import disp
import get_time
import time


#alarm.main_alarm()
#get_TH.get_TH()

while True:
    times = get_time.get_time()
    THs = get_TH.get_TH()

    disp.set_disp(times, THs)
