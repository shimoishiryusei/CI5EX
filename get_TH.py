import grovepi
import math

def get_TH(sensor):
    blue = 0
    white = 1

    try:
        [temp,humidity] = grovepi.dht(sensor, blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            #print("temp = %.02f c humidity = %.02f%%"%(temp, humidity))
            return temp, humidity
    
    except IOError:
        print("Error")

