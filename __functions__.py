#Functions

def clear():
  '''clears all the text on the screen.'''
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
  '''Writes logs.'''
  log_file=open(".logs", "a")
  log_file.write(f"=> {current_time('now')} : {log}\n")
  log_file.close

def show_databse():
  '''This functions shows all the databases present in the database directory.'''
  import os
  directory=os.listdir(path="Databases/")
  serial_number=0
  for databases in directory:
    serial_number+=1
    print(f"{serial_number}. {databases}")

def style_reset():
  from colorama import Style
  print(Style.RESET_ALL)