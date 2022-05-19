import time
import grovepi

buzzer = 8

grovepi.pinMode(buzzer, "OUTPUT")

def main_alarm(B):
    while True:
        try:
            if B == 0:
                grovepi.digitalWrite(buzzer,1)
                print("start")
                break

            elif B == 1:
                grovepi.digitalWrite(buzzer,0)
                print("stop")
                break
                
        except KeyboardInterrupt:
            grovepi.digitalWrite(buzzer,0)
            break
        except IOError:
            print("Error")
