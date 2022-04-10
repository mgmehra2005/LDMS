#Functions

def clear():
  import os
  try:
    os.system("cls")
  except Exception as error:
    e=error
  try:
    os.system("clear")
  except Exception as error:
    e=error