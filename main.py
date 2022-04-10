#In this project i will try to create local database with python dictonery.

#Imported Modules
from tabulate import tabulate
from functools import reduce

#Start
database = {}
print("\n-> MENU\n")
options = ["Create Database",
           "Delete Database",
           "Show Databases"]
option_number=0
for items in options:
  option_number = option_number + 1
  print(f"{option_number}. {items}")

user_choice=int(input('\nChoose the option : '))

if (user_choice==1):
  print(f"\n>> Create Database")