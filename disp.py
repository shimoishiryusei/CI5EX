from grove_rgb_lcd import *

def set_disp(times):
    setText("{}年{}月{}日{}時{}分{}秒".format(time[0], time[1], time[2], time[3], time[4], time[5]))
    setRGB(0,128,64)

    for c in range(0,255):
        setRGB(c,255-c,0)
        time.sleep(0.01)

    setRGB(0,255,0)
    setText("Bye bye, this should wrap")