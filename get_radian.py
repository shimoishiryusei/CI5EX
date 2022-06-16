import grovepi

def get_degree():
    try:
        sensor_value = grovepi.analogRead(potentiometer)
        return sensor_value
        
    except IOError:
        print("Error")