import datetime
dt_now = datetime.datetime.now()

Year = dt_now.year
Month = dt_now.month
Day = dt_now.day
Hour = dt_now.hour
Minute = dt_now.minute
Second = dt_now.second

#print("{}年{}月{}日{}時{}分{}秒".format(Year, Month, Day, Hour, Minute, Second))

def get_time():
    return Year,Month,Day,Hour,Minute,Second