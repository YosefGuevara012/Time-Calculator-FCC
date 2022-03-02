def add_time(start, duration):

  # Splitting the start and duration times

  hour_1, minutes_1, period = time_split(start)
  hour_2, minutes_2         = time_split(duration)

  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  # Calculating minutes and additional hours

  minutes = int(minutes_1) + int(minutes_2)
  hours  += minutes // 60
  minutes = minutes % 60
  
  # Calculating the Initial days and hours
  
  if period == "PM":
    hour_1 = int(hour_1) + 12
    
  hours = int(hour_1) + int(hour_2)
  days = hours // 24
  hours = hours % 24

  # Ajusting the time and the period

  if hours == 12:
    period = "PM"
  elif hours == 0:
    hours = 12
  elif hours > 12:
    period = "PM"
    hours -= 12
  elif hours < 12:
    period = "AM"

    
  return [hours, '{:02}'.format(minutes), period]

def time_split(string):

  hours, minutes = string.split(":")

  try:
    minutes, period = minutes.split(" ")
    return [hours, minutes, period]
  
  except:
    minutes = minutes
    return [hours, minutes]
