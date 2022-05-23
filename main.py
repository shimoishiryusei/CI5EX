# -*- coding: utf-8 -*-
import alarm
import get_TH
import disp
import get_time
import time
import button


#alarm.main_alarm()
#get_TH.get_TH()
H = 13
#M = 40

while True:
    times = get_time.get_time()
    THs = get_TH.get_TH()
    B = button.get_button()

    disp.set_disp(times, THs)
    if times[3] == H :
        print("Test")
        alarm.main_alarm(B)
 



