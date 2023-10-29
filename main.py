
# In this project i will try to create local database with python. This is 
# very useful when we  have a program
# which always sends or records data. To create a backup of that data when 
# the there is any problem on server
# or any network issue this programs records each and every data and send it
# to the server when everything gets fixed.

# Imported Modules
from __functions__ import clear, logs, show_database, style_reset, write_column, MkDBFolder, headerlogo, MsgHeader, ShowTables
from colorama import Fore
import os
import time

# Start
@headerlogo
def main() -> None:

  try:
      user_choice = "input taker"
      while user_choice != 99:
          print("\n-> MENU\n")
          options = [
              "Create Database",
              "Show Databases",
              "Drop Database",
              "Work with Tables"
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
              "Create Databases, If they are not exists."
              print("\n>> Create Database")
              db_name = input("\nDatabase Name : ").lower()
              db_availability = os.path.isfile(f"Databases/{db_name}.py")
              if db_availability:
                  print(Fore.RED + f"\nDatabase {db_name} is already Exist.")
                  style_reset()
                  logs("Database {db_name} is already Exist.")
              else:
                  db_path = f"Databases/{db_name}.py"
                  create_db = open(db_path, "x")
                  create_db.write(f'# {db_name}\n')
                  create_db.write("tables = []\n")
                  create_db.close()
                  print(Fore.GREEN + "Database Created Successfully.")
                  style_reset()
              logs(f"Database {db_name} created successfully.")
              time.sleep(3)
              clear()
              continue
  
          elif user_choice == 2:
              print("\n>> Databases\n")
              show_database()
              logs("Databases shown Successfully.")
              time.sleep(5)
              clear()
              continue
  
          elif user_choice == 3:
              print("\n>> Dropping Database\n")
              show_database()
              db_name = input("\nDatabase name : ").lower()
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
              show_database()
              selected_database = None
              select_database = input("\nSelect Database : ").lower()
              db_availability = os.path.isfile(f"Databases/{select_database}.py")
              if db_availability:
                  selected_database = open(f"Databases/{select_database}.py", "a")
                  print(Fore.GREEN + f"Database {selected_database} selected successfully.")
                  clear()
                
                  print("\n>> Work With Tables\n")
                  option = ["Create Table", "Add Rows"]
                  numbers = 1
                  for options in option:
                      print(f"{numbers}. {options}")
                      numbers += 1
                  decision = int(input("\nChoose the option : "))
                  if decision == 1:
                      clear()
                      print("\n>> Create Table\n")
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
                  

            # TODO: Add row Function
            # TODO: Drop Table Function
            # TODO: Modify Table Function
                  elif decision == 2:
                    clear()
                    print("\n>> Add Row\n")
                    ShowTables(selected_database)
                    print("-"*20)
                    table_name = input("Enter table name : ")
                    
                    style_reset()
                    time.sleep(3)
                    clear()
                    
                    
              else:
                  print(Fore.RED +"Database not found.\nPlease recheck the database name.")
                  style_reset()
                  time.sleep(3)
                  logs(f"Error -> Database '{select_database}' not found.")
                  clear()
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

if __name__ == "__main__":
  # checking depenencies
  MsgHeader("Checking Dependencies....")
  MkDBFolder()
  MsgHeader("Starting Program....")
  time.sleep(2)
  main()
  
# End
