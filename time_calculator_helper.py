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
  elif hours > 12:
    period = "PM"
    hours -= 12
  elif hours < 12:
    period = "AM"


  # Calculating the end day

  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  if day != None:
    day = day.capitalize()
    index = (days % 7) + week.index(day)
    

    # Ajusting the text result format
    if days == 0:
      txt = "{0}:{1} {2}, {3}".format(hours,'{:02}'.format(minutes),period,week[index])
    elif days == 1:
      txt = "{0}:{1} {2}, {3}  (next day)".format(hours,'{:02}'.format(minutes),period, week[index])
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


print("3:00 PM,3:10")
print(add_time("3:00 PM", "3:10"))
print("********************************")

print("11:30 PM,2:32")
print(add_time("11:30 AM", "2:32", "Monday"))
print("********************************")

print("11:30 PM,2:32")
print(add_time("11:43 AM", "00:20"))
print("********************************")

print("10:10 PM, 3:30")
print(add_time("10:10 PM", "3:30"))
print("********************************")

print("11:43 PM, 24:20")
print(add_time("11:43 PM", "24:20", "tueSday"))
print("********************************")

print("6:30 PM, 205:12")
print(add_time("6:30 PM", "205:12"))
print("********************************")
