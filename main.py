# -*- coding: utf-8 -*-
# imports
import alarm
import get_TH
import disp
import get_time
import time
import Notify
import button

# define
buzzer = 8
button_num = 3
sensor = 4
count_Button = 0
chack = 0

# set timer
H = input("Hour:")
M = input("Minute:")

# move
while True:
    times = get_time.get_time()
    THs = get_TH.get_TH(sensor)
    B = button.get_button(button_num)

    disp.set_disp(times, THs)
    if times[3] == int(H) & times[4] == int(M):
        chack += alarm.main_alarm(buzzer, B, count_Button)
        if chack >= 1:
            count_Button += 1
            Notify.main()


 



