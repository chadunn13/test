import datetime

def main():
	getDateToday()

def getDateToday():
	month_tuple = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
	date_today = datetime.date.today()
	month_num = date_today.month
	month_say = month_tuple[month_num]
	day_say = date_today.day
	year_say = date_today.year
	date_say = "Today is " + month_say + " " + day_say + ", " + year_say + ", Master"
	print(date_say)
  
def getTimeNow():
	
  
if __name__ == "__main__":
	main()# your code goes here
