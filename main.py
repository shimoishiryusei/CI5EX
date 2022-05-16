# -*- coding: utf-8 -*-
import alarm
import get_TH
import disp
import get_time

items = get_time.get_time()

#alarm.main_alarm()
get_TH.get_TH()

disp.set_disp(items)
