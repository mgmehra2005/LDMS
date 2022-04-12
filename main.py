#In this project i will try to create local database with python dictonery.

#Imported Modules
from tabulate import tabulate
from functools import reduce
import __functions__
from __functions__ import logs
import colorama
import os
import time

#Start
user_choice="input taker"
while (user_choice != 99):
  try:
    print("\n-> MENU\n")
    options = ["Create Database",
             "Show Databases",
             "Delete Database",
             "Select Database"]
    option_number=0
    for items in options:
      option_number = option_number + 1
      print(f"{option_number}. {items}")
    print("99. To Exit")

    user_choice=int(input('\nChoose the option : '))      #User input
    __functions__.clear()

  #Conditions
    if (user_choice==1):
      print(f"\n>> Create Database")
      db_name=input("\nDatabase Name : ")
      db_availablity=os.path.isfile(f"Databases/{db_name}")
      if db_availablity:
        print(f"\nDatabase {db_name} is already Exist.")
        logs("Database {db_name} is already Exist.")  
      else:  
        db_path=f"Databases/{db_name}"
        create_db=open(db_path, "x")
        create_db.close()
        print("\nDatabase Created Successfully.")
      logs(f"Database {db_name} created successfully.")
      time.sleep(3)
      __functions__.clear()
      continue

    elif (user_choice==2):
      print(f"\n>> Databases\n")
      __functions__.show_databse()
      logs("Databases shown Successfully.")

    elif (user_choice==3):
      print(f"\n>> Dropping Database\n")
      __functions__.show_databse()
      db_name=input("\nDatabase name : ")
      try:
        os.system(f"rm Databases/{db_name}")
        print("Database removed successfully.")
        logs(f"Database {db_name} is removed successfully.")
        time.sleep(3)
        __functions__.clear()
        continue
      except Exception as error:
        print("\nThere is an eroor while removing database.")
        user_input=input("\nDo you want to see the error (y/n) : ")
        if (user_input=="y"):
          print(error)
          time.sleep(5)
          break
        elif (user_input=="n"):
          print("\nSorry for the interruption.")
        logs(f"Error -> {error}")
        break

  except Exception as program_error:
    print("\nThere is an eroor while running the program.")
    user_input=input("\nDo you want to see the error (y/n) : ")
    if (user_input=="y"):
      print(program_error)
      time.sleep(5)
      break
    elif (user_input=="n"):
      print("\nSorry for the interruption.")
    logs(f"Error -> {program_error}")
    break
print("Thanks for using Local Database System.")
time.sleep(4)
#End