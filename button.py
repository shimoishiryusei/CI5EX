import time
import grovepi

button = 3

grovepi.pinMode(button, "INPUT")

def get_button():
    while True:
        try:
            return grovepi.digitalRead(button)
        except:
            print("Error")