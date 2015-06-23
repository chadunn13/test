import datetime
from datetime_files import datetimecommands
from datetime_files import datetime2

def main():
  parseInput(input("give a command"))

def parseInput(string_input):
  if string_input in DateTimeCommands.time_now_commands:
    DateTime2.getTimeNow()
  elif string_input in DateTimeCommands.date_today_commands:
    DateTime2.getDateToday()

  
if __name__ == "__main__":
  main()
