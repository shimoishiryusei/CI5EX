import grovepi
import math

sensor = 4

blue = 0
white = 1

def get_TH():
    while True:
        try:
            [temp,humidity] = grovepi.dht(sensor, blue)
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                #print("temp = %.02f c humidity = %.02f%%"%(temp, humidity))
                return temp, humidity
        
        except IOError:
            print("Error")

