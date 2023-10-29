# This file includes all the functions used in this Program.

# Imported Modules
import settings
from colorama import Style, Fore
import os
import datetime

def clear() -> None:
    """ clears all the text on the screen. """
    try:
        if settings.Linux is True:
            os.system("clear")
        elif settings.Windows is True:
            os.system("cls")
    except Exception as error:
        e = error


def current_time(time_parameter):
    """ Parameters : full_time, hour, minute, now """
    
    clock = datetime.datetime.now()
    result = None
    if time_parameter == "full_time":
        result = f"{clock.hour} : {clock.minute}"
    elif time_parameter == "hour":
        result = clock.hour
    elif time_parameter == "minute":
        result = clock.minute
    elif time_parameter == "now":
        result = clock
    return result


def logs(log) -> None:
    """ Writes logs. """
    if settings.Write_Logs is True:
        log_file = open(".logs", "a")
        log_file.write(f"=> {current_time('now')} : {log}\n")
        log_file.close()
    elif settings.Write_Logs is False:
        log_file = open(".logs", "a")
        log_file.write("=> Anonymous Action")
        log_file.close()

def show_database() -> None:
    """This functions shows all the databases present in the database directory."""
    
    directory = os.listdir(path="Databases/")
    serial_number = 0
    for databases in directory:
        serial_number += 1
        print(f"{serial_number}. {databases[:-3]}")


def style_reset() -> None:
    """Resets all the style."""
    print(Style.RESET_ALL)


def write_column(columns, 
                 database, 
                 table) -> None:
  
    """Create columns in tables."""
    
    selected_database = open(f"Databases/{database}.py", "a")
    try:
        selected_database.write(f"tables.append('{table}')\n")
        selected_database.write(f"{table}_property ="+" {}\n")
        selected_database.write(f"{table}_property['columns'] = {columns}\n")
        selected_database.write(f"{table} = []\n")
      
        logs(f"Columns Written Successfully in table {table}.")
    except Exception as error:
        e = error
        logs(f"Error -> {e}")
        print(Fore.RED + "There is an error while writing columns.")
    selected_database.close()


def MkDBFolder(FolderName: str="Databases") -> None:
  """Creates folder for databases."""

  if os.path.exists(FolderName) is False:
    try:
      os.mkdir(FolderName)
      logs(f"Folder '{FolderName}' created.")
    except Exception as e:
      logs(f"Error -> {e}")
  else:
    logs("DB Folder already exist.")
    pass

def headerlogo(func):
  def fx(*args, **kwargs):
    clear()
    print("""
 _     ____  __  __ ____  
| |   |  _ \|  \/  / ___| 
| |   | | | | |\/| \___ \ 
| |___| |_| | |  | |___) |
|_____|____/|_|  |_|____/ 
""".center(50), "\n")
    result = func(*args, **kwargs)
    return result
  return fx

@headerlogo
def MsgHeader(message: str) -> None:
  print(message)
  logs(message)

def ShowTables(database_name) -> None:
  """Shows all the tables present in the database."""
  
  try:
    from Databases import database_name as db

    print(f"{Fore.GREEN}Tables Present in Database : ")
    for index, tables in enumerate(db.tables, start=1):
      print(f"{index}. {tables}")
    
  except Exception as error:
    e = error
    logs(f"Error -> {e}")
    