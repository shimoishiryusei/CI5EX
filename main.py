# -*- coding: utf-8 -*-
import alarm
import get_TH
import disp
import get_time
import time
import button


#alarm.main_alarm()
#get_TH.get_TH()
count_B = 0
H = 15
#M = 40

while True:
    times = get_time.get_time()
    THs = get_TH.get_TH()
    B = button.get_button()

    disp.set_disp(times, THs)
    if times[3] == H :
        print("Test")
        if count_B == 0:
            alarm.main_alarm(B)
            count_B += 1
            print(count_B)



