def add_time(start, duration):

  # Spliting the start and duration times

  hour_1, minutes_1, period = time_split(start)
  hour_2, minutes_2         = time_split(duration)

  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  # Calculating the Initial days and hours

  hours = int(hour_1) + int(hour_2)
  days = hours // 24
  hours = hours % 24

  # Calculating minutes and additional hours

  minutes = int(minutes_1) +int(minutes_2)
  add_hours = minutes // 60
  minutes = minutes % 60
  



  return [days, hours]

def time_split(string):

  hours, minutes = string.split(":")

  try:
    minutes, period = minutes.split(" ")
    return [hours, minutes, period]
  
  except:
    minutes = minutes
    return [hours, minutes]


    

