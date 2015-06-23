import datetime
from datetime_files import datetimecommands
from datetime_files import datetime2

def main():
  parseInput(raw_input("give a command"))

def parseInput(string_input):
  if string_input in datetimecommands.DateTimeCommands.time_now_commands:
    datetime2.getTimeNow()
  elif string_input in datetimecommands.DateTimeCommands.date_today_commands:
    datetime2.getDateToday()


if __name__ == "__main__":
  main()
