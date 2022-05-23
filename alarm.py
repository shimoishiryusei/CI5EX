import time
import grovepi

def main_alarm(buzzer, B, count_B):
    Buzzzer_on = 0
    Buzzzer_off = 1
    grovepi.pinMode(buzzer, "OUTPUT")
    while True:
        try:
            if B == 0 & count_B == 0:
                grovepi.digitalWrite(buzzer,1)
                return Buzzzer_on
                break

            elif B == 1:
                count_B += 1
                grovepi.digitalWrite(buzzer,0)
                return Buzzzer_off
                break
                
        except KeyboardInterrupt:
            grovepi.digitalWrite(buzzer,0)
            break
        except IOError:
            print("Error")
