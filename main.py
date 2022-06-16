# -*- coding: utf-8 -*-
# imports
from tabnanny import check
import alarm
import get_TH
import disp
import get_time
import time
import Notify
import button
import Light

# define
buzzer = 8
button_num = 3
sensor = 4
count_Button = 0
check = 0
LINE_flag = 0
alarm_flag = 0
light_flag = 0

# set timer
H = input("Hour:")
M = input("Minute:")

# move
while True:
    times = get_time.get_time()
    THs = get_TH.get_TH(sensor)
    B = button.get_button(button_num)
    Light_val = Light.get_light()

    disp.set_disp(times, THs)
    if Light_val < 100 and light_flag == 0:
        Notify.send_line_notify(2)
        light_flag = 1
    
    if times[3] == int(H) and times[4] == int(M):
        if check >= 1:
            count_Button += 1
            if LINE_flag == 0:
                Notify.send_line_notify(1)
                LINE_flag = 1
                light_flag = 0

        else:
            if alarm_flag == 0:
                check += alarm.main_alarm(buzzer, B, count_Button)
    else:
        count_Button = 0
        check = 0
        LINE_flag = 0
        alarm_flag = 0
    



 



