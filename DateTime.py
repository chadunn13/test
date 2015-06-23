import datetime
import master
import IO

def getDateToday():
  month_tuple = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
  date_today = datetime.date.today()
  month_num = date_today.month
  month_say = month_tuple[month_num]
  day_say = date_today.day
  year_say = date_today.year
  date_say = "Today is " + month_say + " " + str(day_say) + ", " + str(year_say) + ", " + master.name
  IO.say(date_say)

def getTimeNow():
  time_now = datetime.time.time()
  hour_num = time_now.hour
  hour_say = 0
  am_pm_say = ""
  
  if hour_num == 0:
    hour_say = 12
    am_pm_say = "AM"
  elif hour_num < 12:
    hour_say = hour_num
    am_pm_say = "AM"
  elif hour_num == 12:
    hour_say = 12
    am_pm_say = "PM"
  else:
    hour_say = str(hour_num - 12)
    am_pm_say = "PM"
    
  minute_say = time_now.minutes
  time_say = "The time is" + hour_say + " " + minute_say + " " + am_pm_say
