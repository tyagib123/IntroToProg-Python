# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# bhawnat , November 16th, 2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for strData in objFile:
    Task, Priority = strData.rstrip('\n').split(',')  # rstrip() will remove the newline character from the right side.
    dicRow[Task] = Priority
objFile.close()
for line in dicRow.items():
    lstRow = ({line[0] + ':' + line[1]})
    lstTable.append(lstRow)


# Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print(lstTable)
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        task = input("Enter new item")
        priority = input("Enter new price of an item")
        lstRow = ({task.lstrip(' ') + ':' + priority.lstrip(' ')})
        lstTable.append(lstRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        removeItem = int(input("Provide the index of the element you want to remove from the list"))
        lstTable.pop(removeItem)
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", "w")  # Opening the file in write mode
        for item in lstTable:  # Iterating through the list using item variable
            for k in item:  # Fetching the key, value pair in an item variable
                strRow = str(k) # Converting the key,value pair into string first
                splitRow = strRow.split(':') # Splitting the row on : separator
                objFile.write(splitRow[0] + ',' + splitRow[1] + '\n')  # Finally writing to the file.
        objFile.close()
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Exiting from the program")
        break