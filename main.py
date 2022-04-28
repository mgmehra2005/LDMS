#In this project i will try to create local database with python dictonery.

#Imported Modules
from tabulate import tabulate
from functools import reduce
import __functions__
from __functions__ import logs
from __functions__ import style_reset
from colorama import Fore
import os
import time

#Start
try:
    user_choice = "input taker"
    while (user_choice != 99):
        print("\n-> MENU\n")
        options = [
            "Create Database", "Show Databases", "Delete Database",
            "Edit Database"
        ]
        option_number = 0
        for items in options:
            option_number = option_number + 1
            print(f"{option_number}. {items}")
        print("99. To Exit")

        user_choice = int(input('\nChoose the option : '))  #User input
        __functions__.clear()

        #Conditions
        if (user_choice == 1):
            print(f"\n>> Create Database")
            db_name = input("\nDatabase Name : ")
            db_availablity = os.path.isfile(f"Databases/{db_name}")
            if db_availablity:
                print(Fore.RED + f"\nDatabase {db_name} is already Exist.")
                style_reset()
                logs("Database {db_name} is already Exist.")
            else:
                db_path = f"Databases/{db_name}"
                create_db = open(db_path, "x")
                create_db.close()
                print(Fore.GREEN + "Database Created Successfully.")
                style_reset()
            logs(f"Database {db_name} created successfully.")
            time.sleep(3)
            __functions__.clear()
            continue

        elif (user_choice == 2):
            print(f"\n>> Databases\n")
            __functions__.show_databse()
            logs("Databases shown Successfully.")
            time.sleep(5)
            __functions__.clear()
            continue

        elif (user_choice == 3):
            print(f"\n>> Dropping Database\n")
            __functions__.show_databse()
            db_name = input("\nDatabase name : ")
            try:
                os.system(f"rm Databases/{db_name}")
                print(Fore.GREEN + "Database removed successfully.")
                style_reset()
                logs(f"Database {db_name} is removed successfully.")
                time.sleep(3)
                __functions__.clear()
                continue
            except Exception as error:
                print(Fore.RED +
                      "\nThere is an eroor while removing database.")
                style_reset()
                user_input = input("\nDo you want to see the error (y/n) : ")
                if (user_input == "y"):
                    print(error)
                    time.sleep(5)
                    break
                elif (user_input == "n"):
                    print("\nSorry for the interruption.")
                logs(f"Error -> {error}")
                break
        elif (user_choice == 4):
            option=["", "Create Table", "Edit Table"]
            print()
            if (user_choice == 4):
                print(f"\n>> Create Table\n")
                __functions__.show_databse()
                select_database = input("\nEnter database name : ")
                db_availablity = os.path.isfile(f"Databases/{select_database}")
                if db_availablity:
                    selected_database = open(f"Databases/{select_database}", "a")
                    print(Fore.GREEN + "Database selected successfully.")
                    style_reset()
                    table_name=input("Enter table name : ")
                    selected_database.write(f"{table_name} = dict()\n")
                    print(Fore.GREEN + "Table created successfully.")
                    style_reset()
                    logs(f"Table {table_name} created successfully.")
                    time.sleep(3)
                    __functions__.clear()
                else:
                    print(Fore.RED +
                          "Database not found.\nPlease recheck the database name.")
                    style_reset()
                    time.sleep(3)
                    break
                    logs(f"Error -> {error}")

    print(Fore.YELLOW + "Thanks for using Local Database System.")
    time.sleep(4)

except Exception as program_error:
    print(Fore.RED + "\nThere is an eroor while running the program.")
    style_reset()
    user_input = input("Do you want to see the error (y/n) : ")
    if (user_input == "y"):
        print(program_error)
        time.sleep(5)
    elif (user_input == "n"):
        print("\nSorry for the interruption.")
    logs(f"Error -> {program_error}")

#End
