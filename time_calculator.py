def add_time(start, duration, day = None):


  # Spliting the start and duration times

  hour_1, minutes_1, period = time_split(start)
  hour_2, minutes_2         = time_split(duration)



  # Calculating minutes and additional hours

  minutes = int(minutes_1) + int(minutes_2)
  hours   = minutes // 60
  minutes = minutes % 60

  # Calculating the Inicial days and hours

  if period == "PM":
    hour_1 = int(hour_1) + 12

  hours +=  int(hour_1) + int(hour_2)
  days = hours // 24
  hours = hours % 24


  # Ajusting the time and the period

  if hours == 12:
    period = "PM"
  elif hours == 0:
    hours = 12
    period = "AM"
  elif hours > 12:
    period = "PM"
    hours -= 12
  elif hours < 12:
    period = "AM"


  # Calculating the end day

  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  if day != None:
    day = day.capitalize()
    index = days + week.index(day)
    index = index % 7
    

    # Ajusting the text result format
    if days == 0:
      txt = "{0}:{1} {2}, {3}".format(hours,'{:02}'.format(minutes),period,week[index])
    elif days == 1:
      txt = "{0}:{1} {2}, {3} (next day)".format(hours,'{:02}'.format(minutes),period, week[index])
    elif days > 1:
      txt = "{0}:{1} {2}, {3} ({4} days later)".format(hours,'{:02}'.format(minutes),period, week[index], days)

  else:
    
     # Ajusting the text result format
    if days == 0:
      txt = "{0}:{1} {2}".format(hours,'{:02}'.format(minutes),period)
    elif days == 1:
      txt = "{0}:{1} {2} (next day)".format(hours,'{:02}'.format(minutes),period)
    elif days > 1:
      txt = "{0}:{1} {2} ({3} days later)".format(hours,'{:02}'.format(minutes),period, days)
    
  return txt

def time_split(string):

  hours, minutes = string.split(":")

  try:
    minutes, period = minutes.split(" ")
    return [hours, minutes, period]
  
  except:
    minutes = minutes
    return [hours, minutes]
