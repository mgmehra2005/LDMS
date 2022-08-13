# In this project i will try to create local database with python. This is very useful when we  have a program
# which always sends or records data. To create a backup of that data when the there is any problem on server
# or any network issue this programs records each and every data and send it to the server when everything gets fixed.

# Imported Modules
from tabulate import tabulate
from functools import reduce
import settings
from __functions__ import *
from colorama import Fore
import os
import time

# Start
try:
    user_choice = "input taker"
    while user_choice != 99:
        print("\n-> MENU\n")
        options = [
            "Create Database",
            "Show Databases",
            "Delete Database",
            "Edit Database"
        ]
        option_number = 0
        for items in options:
            option_number = option_number + 1
            print(f"{option_number}. {items}")
        print("99. To Exit")

        user_choice = int(input('\nChoose the option : '))  # User input from menu
        clear()

        # Conditions
        if user_choice == 1:
            print(f"\n>> Create Database")
            db_name = input("\nDatabase Name : ")
            db_availability = os.path.isfile(f"Databases/{db_name}.py")
            if db_availability:
                print(Fore.RED + f"\nDatabase {db_name} is already Exist.")
                style_reset()
                logs("Database {db_name} is already Exist.")
            else:
                db_path = f"Databases/{db_name}.py"
                create_db = open(db_path, "x")
                create_db.write(f"""class {db_name}:
    pass
""")
                create_db.close()
                print(Fore.GREEN + "Database Created Successfully.")
                style_reset()
            logs(f"Database {db_name} created successfully.")
            time.sleep(3)
            clear()
            continue

        elif user_choice == 2:
            print(f"\n>> Databases\n")
            show_database()
            logs("Databases shown Successfully.")
            time.sleep(5)
            clear()
            continue

        elif user_choice == 3:
            print(f"\n>> Dropping Database\n")
            show_database()
            db_name = input("\nDatabase name : ")
            try:
                os.system(f"rm Databases/{db_name}.py")
                print(Fore.GREEN + "Database removed successfully.")
                style_reset()
                logs(f"Database {db_name} is removed successfully.")
                time.sleep(3)
                clear()
                continue
            except Exception as error:
                print(Fore.RED +
                      "\nThere is an error while removing database.")
                style_reset()
                user_input = input("\nDo you want to see the error (y/n) : ")
                if user_input == "y":
                    print(error)
                    time.sleep(5)
                    break
                elif user_input == "n":
                    print("\nSorry for the interruption.")
                logs(f"Error -> {error}")
                break
        elif user_choice == 4:
            clear()
            option = ["Create Table", "Edit Table"]
            numbers = 1
            for options in option:
                print(f"{numbers}. {options}")
                numbers += 1
            decision = int(input("\nChoose the option : "))
            if decision == 1:
                clear()
                print(f"\n>> Create Table\n")
                show_database()
                select_database = input("\nEnter database name : ")
                db_availability = os.path.isfile(f"Databases/{select_database}.py")
                if db_availability:
                    selected_database = open(f"Databases/{select_database}.py", "a")
                    print(Fore.GREEN + "Database selected successfully.")
                    style_reset()
                    table_name = input("Enter table name : ")
                    selected_database.write(f"{table_name} = {select_database}()\n")
                    column_names = input("Enter column names separated by ',' :  ").split(",")
                    print(Fore.GREEN + "Table created successfully.")
                    style_reset()
                    logs(f"Table {table_name} created successfully.")
                    write_column(column_names, select_database, table_name)
                    time.sleep(3)
                    clear()
                else:
                    print(Fore.RED +
                          "Database not found.\nPlease recheck the database name.")
                    style_reset()
                    time.sleep(3)
                    logs(f"Error -> Database '{select_database}' not found.")
                    continue

    print(Fore.YELLOW + "Thanks for using Local Database System.")
    time.sleep(4)

except Exception as program_error:
    print(Fore.RED + "\nThere is an error while running the program.")
    style_reset()
    user_input = input("Do you want to see the error (y/n) : ")
    if user_input == "y":
        print(program_error)
        time.sleep(5)
    elif user_input == "n":
        print("\nSorry for the interruption.")
    logs(f"Error -> {program_error}")

# End
