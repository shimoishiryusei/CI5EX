import time
import grovepi

def get_button(button):
    grovepi.pinMode(button, "INPUT")
    
    try:
        return grovepi.digitalRead(button)
    except:
        print("Error")