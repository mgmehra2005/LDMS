#In this project i will try to create local database with python dictonery.

#Imported Modules
from tabulate import tabulate
from functools import reduce
import __functions__
import colorama

#Start

try:
  databases = {}
  log_file=open(".logs", "a")
  print("\n-> MENU\n")
  options = ["Create Database",
           "Delete Database",
           "Show Databases"]
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
    db_path=f"Databases/{db_name}"
    create_db=open(db_path, "x")
    create_db.close()
    __functions__.logs(f"Database {db_name} created successfully.")
    print("\nDatabase Created Successfully.")

  log_file.close()

except Exception as program_error:
  print("\nThere is an eroor while running the program.")
  user_input=input("\nDo you want to see the error (y/n) : ")
  if (user_input=="y"):
    print(program_error)
  elif (user_input=="n"):
    print("\nSorry for the interruption.")

#End