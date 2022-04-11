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

try:
  print("\n-> MENU\n")
  options = ["Create Database",
           "Show Databases",
           "Delete Database"]
  option_number=0
  for items in options:
    option_number = option_number + 1
    print(f"{option_number}. {items}")
  print("99. To Exit")

  user_choice=int(input('\nChoose the option : '))
  __functions__.clear()

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
    except Exception as error:
      print("\nThere is an eroor while removing database.")
      user_input=input("\nDo you want to see the error (y/n) : ")
      if (user_input=="y"):
        print(program_error)
      elif (user_input=="n"):
        print("\nSorry for the interruption.")
      logs(f"Error -> {error}")
    
except Exception as program_error:
  print("\nThere is an eroor while running the program.")
  user_input=input("\nDo you want to see the error (y/n) : ")
  if (user_input=="y"):
    print(program_error)
  elif (user_input=="n"):
    print("\nSorry for the interruption.")
  logs(f"Error -> {program_error}")

#End