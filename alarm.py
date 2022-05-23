import time
import grovepi

def main_alarm(buzzer, B, count_B):
    Buzzzer_on = 0
    Buzzzer_off = 1
    grovepi.pinMode(buzzer, "OUTPUT")
    try:
        if B == 0:
            if count_B == 0:
                grovepi.digitalWrite(buzzer,1)
                return Buzzzer_on
            
            elif count_B != 0:
                grovepi.digitalWrite(buzzer,0)
                return Buzzzer_off
            

        elif B == 1:
            grovepi.digitalWrite(buzzer,0)
            return Buzzzer_off
        
    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
    
    except IOError:
        print("Error")
