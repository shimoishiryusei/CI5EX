import datetime

def get_time():
    dt_now = datetime.datetime.now()

    Year = dt_now.year
    Month = dt_now.month
    Day = dt_now.day
    Hour = dt_now.hour
    Minute = dt_now.minute
    Second = dt_now.second

    return Year,Month,Day,Hour,Minute,Second
