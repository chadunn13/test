
def parseInput(string_input):
  if string_input in DateTimeCommands.time_now_commands:
    DateTime2.getTimeNow()
  elif string_input in DateTimeCommands.date_today_commands:
    DateTime2.getDateToday()
