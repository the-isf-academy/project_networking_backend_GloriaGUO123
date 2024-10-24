from datetime import datetime, time, timedelta, timezone
def allocating_time_period(input_time):
    #Morning: 4:00 AM to 11:59 AM
    if time(4, 0) <= input_time < time(12, 0):
        return "Morning"
    #Afternoon: 12:00 PM to 5:59 PM
    elif time(12, 0) <= input_time < time(18, 0):
        return "Afternoon"
    #Evening: 6:00 PM to 3:59 AM
    else:
        return "Evening"