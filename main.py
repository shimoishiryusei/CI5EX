# -*- coding: utf-8 -*-
# imports
import alarm
import get_TH
import disp
import get_time
import time
import button

# define
buzzer = 8
button_num = 3
sensor = 4
count_Button = 0
chack = 0

H = 13
#M = 40

while True:
    times = get_time.get_time()
    THs = get_TH.get_TH(sensor)
    B = button.get_button(button_num)

    disp.set_disp(times, THs)
    if times[3] == H :
        print("Test")
        chack += alarm.main_alarm(buzzer, B, count_Button)
        if chack == 1:
            count_Button += 1
 



