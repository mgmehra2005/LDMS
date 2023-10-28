# Local Database System
This program aims to create a local database system. It includes three main files: main.py, __functions__.py, and settings.py.

main.py:

The code starts by importing various modules like clear, current_time, logs, and others from the __functions__.py file at the beginning using the import statement.
It defines a function main() which serves as the entry point of the program.
Inside the main() function, there is a menu loop that prompts the user to choose different options related to creating, showing, and managing databases.
Depending on the user's selection, the program performs tasks like creating a database, showing existing databases, dropping a database, and expanding a database. It handles these operations by interacting with files in the Databases directory.
The code also includes placeholders (TODO) for additional functions related to adding rows, dropping tables, and modifying tables. These functions are not implemented in the provided code.
The main script includes error handling using try-except blocks to catch and display any exceptions that occur during the program's execution.
__functions__.py:

This file contains various utility functions used in the main program.
It includes functions like clear() to clear the screen, current_time() to get the current time, logs() for writing logs, show_database() to list the available databases, style_reset() to reset styles, write_column() to create columns in tables, MkDBFolder() to create a folder for databases, headerlogo() and MsgHeader() for displaying headers in the console.
These functions provide reusable code blocks and help in organizing and performing specific tasks in the program.
settings.py:

This file serves as a configuration file for the program. It includes various settings that can be toggled on or off by changing the boolean values.
The settings include the program name (ProgramName), the operating system (Windows and Linux), and the option to write logs (Write_Logs).

In summary, this code creates a local database system using a combination of menu-driven logic, utility functions, and configuration settings. It allows users to perform operations like creating, showing, and managing databases. The __functions__.py file provides reusable functions, and the settings.py file allows for customization of the program's behavior.
