import datetime
#import master
#import IO


def getDateToday():
    month_tuple = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    date_today = datetime.date.today()
    month_num = date_today.month
    month_say = month_tuple[month_num]
    day_say = date_today.day
    year_say = date_today.year
    date_say = "Today is " + month_say + " " + str(day_say) + ", " + str(year_say) + ", Master"
    #IO.say(date_say)
    print(date_say)
    
def getTimeNow():
    time_now = datetime.datetime.now().time()
    hour_num = time_now.hour
    hour_say = ""
    am_pm_say = ""

    if hour_num == 0:
      hour_say = 12
      am_pm_say = "AM"
    elif hour_num < 12:
      hour_say = str(hour_num)
      am_pm_say = "AM"
    elif hour_num == 12:
      hour_say = 12
      am_pm_say = "PM"
    else:
      hour_say = str(hour_num - 12)
      am_pm_say = "PM"

    minute_num = time_now.minute
    minute_say = ""
    
    if minute_num == 0:
        minute_say = "o clock"
    elif minute_num < 10:
        minute_say = "o " + str(minute_num)
    else:
        minute_say = str(minute_num)
    time_say = "The time is " + hour_say + " " + minute_say + " " + am_pm_say + ", Master"
    #IO.say(time_say)
    print(time_say)
