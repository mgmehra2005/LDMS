#Functions

def clear():
  import os
  try:
    os.system("cls")
  except Exception as error:
    e=error
  try:
    os.system("clear")
  except Exception as error:
    e=error
  
def current_time(time_parameter):      #Parameters : full_time, hour, minute, now
    import datetime
    clock = datetime.datetime.now()
    if time_parameter == "full_time":
        result=f"{clock.hour} : {clock.minute}"
    elif time_parameter == "hour":
        result=clock.hour
    elif time_parameter == "minute":
        result=clock.minute
    elif (time_parameter == "now"):
        result=clock
    return result

def logs(log):
  log_file=open(".logs", "a")
  log_file.write(f"=> {current_time('now')} : {log}\n")
  log_file.close