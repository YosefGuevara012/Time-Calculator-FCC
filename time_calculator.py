def add_time(start, duration):

  hour_1, minutes_1, period = time_split(start)
  hour_2, minutes_2         = time_split(duration)

  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  # Calculating the Initial days and hours

  hours = int(hour_1) + int(hour_2)
  days = hours // 24
  hours = hours % 24



  return [days, hours]

def time_split(string):

  hours, minutes = string.split(":")

  try:
    minutes, period = minutes.split(" ")
    return [hours, minutes, period]
  
  except:
    minutes = minutes
    return [hours, minutes]


    

