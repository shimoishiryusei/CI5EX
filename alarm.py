import time
import grovepi

grovepi.pinMode(buzzer, "OUTPUT")

while True:
    try:
        grovepi.digitalWrite(buzzer,1)
        print("start")
        time.sleep(1)

        grovepi.digitalWrite(buzzer,0)
        print("stop")
        time.sleep(1)
    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
        break
    except IOError:
        print("Error")
