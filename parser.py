from io.py import IO
from datetime_files.datetimecommands import DateTimeCommands
from datetime_files.datetime2 import DateTime2

class Parser:
  
  def parseInput(string_input):
    if string_input in DateTimeCommands.time_now_commands:
      DateTime2.getTimeNow()
    elif string_input in DateTimeCommands.date_today_commands:
      DateTime2.getDateToday()
      
