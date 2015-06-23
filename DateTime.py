import datetime
import master
import IO

def getDateToday():
  month_tuple = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
  date_today = datetime.date.today()
  month_num = date_today.month
  month_say = month_tuple(month_num)
  day_say = date_today.day
  year_say = date_today.year
  date_say = "Today is " + month_say + " " + day_say + ", " + year_say + ", " + master.name
  IO.say(date_say)
