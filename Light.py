import grovepi

def get_light():
    light_sensor = 1
    grovepi.pinMode(light_sensor,"IMPUT")
    try:

        senesor_value = grovepi.analogRead(light_sensor)
        return senesor_value

    except IOError:
        print("Error")
