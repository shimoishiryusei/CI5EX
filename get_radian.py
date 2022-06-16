import grovepi

def get_degree():
    potentiometer = 0

    grovepi.pinMode(potentiometer, "INPUT")

    try:
        sensor_value = grovepi.analogRead(potentiometer)
        return sensor_value

    except IOError:
        print("Error")