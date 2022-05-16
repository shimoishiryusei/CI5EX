# -*- coding: utf-8 -*-
import alarm
import get_TH
import disp
import get_time
import time


#alarm.main_alarm()
#get_TH.get_TH()

while True:
    items = get_time.get_time()
    disp.set_disp(items)
    time.sleep(1)
