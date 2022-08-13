# This file includes all the functions used in this Program.

# Imported Modules
import settings


def clear():
    """ clears all the text on the screen. """
    import os
    try:
        if settings.Linux is True:
            os.system("clear")
        elif settings.Windows is True:
            os.system("cls")
    except Exception as error:
        e = error


def current_time(time_parameter):
    """ Parameters : full_time, hour, minute, now """
    import datetime
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


def logs(log):
    """ Writes logs. """
    if settings.Write_Logs is True:
        log_file = open(".logs", "a")
        log_file.write(f"=> {current_time('now')} : {log}\n")
        log_file.close()
    elif settings.Write_Logs is False:
        log_file = open(".logs", "a")
        log_file.write(f"=> Anonymous Action")
        log_file.close()

def show_database():
    """This functions shows all the databases present in the database directory."""
    import os
    directory = os.listdir(path="Databases/")
    serial_number = 0
    for databases in directory:
        serial_number += 1
        print(f"{serial_number}. {databases[:-3]}")


def style_reset():
    """Resets all the style."""
    from colorama import Style
    print(Style.RESET_ALL)


def write_column(columns, database, table):
    """Create columns in tables."""
    from colorama import Fore
    selected_database = open(f"Databases/{database}.py", "a")
    try:
        for column in columns:
            selected_database.write(f"{table}.{column} = []\n")
        logs(f"Columns Written Successfully in table {table}.")
    except Exception as error:
        e = error
        print(Fore.RED + "There is an error while writing columns.")
