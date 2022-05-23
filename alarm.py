import time
import grovepi

def main_alarm(buzzer, B, count_B):
    Buzzzer_on = 1
    Buzzzer_off = 0
    grovepi.pinMode(buzzer, "OUTPUT")
    while True:
        try:
            if B == 0 & count_B == 0:
                grovepi.digitalWrite(buzzer,1)
                print("start")
                return Buzzzer_on
                break

            elif B == 1:
                count_B += 1
                grovepi.digitalWrite(buzzer,0)
                print("stop")
                return Buzzzer_off
                break
                
        except KeyboardInterrupt:
            grovepi.digitalWrite(buzzer,0)
            break
        except IOError:
            print("Error")
