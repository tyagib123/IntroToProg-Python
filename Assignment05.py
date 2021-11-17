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
openFile = open(objFile, "r")
for strData in openFile:
    key, value = strData.split(',')  # Splitting the row into key and value pairs
    dicRow = {'Task': key.strip(),
              'Priority': value.strip()}  # Creating dictionary with two columns - Task and Priority
    lstTable.append(dicRow)  # Appending the dictionary in the list
openFile.close()  # Closing the file using close()

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
        task = input("Enter new item")  # Taking new item as user input
        priority = input("Enter new price of an item")  # Taking price of an item as user input
        lstRow = ({"Task": task.strip(), "Priority": priority.strip()})  # Creating new row with both inputs
        lstTable.append(lstRow)  # Adding both as a new row in the list
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        removeItem = str(input("Which item would you like to remove?"))  # Taking item to be removed as user input
        for row in lstTable:  # Looping through each row in the lstTable
            if row['Task'].lower() == removeItem.lower():  # Comparing if the key is equal to the user input
                lstTable.remove(row)  # Removing row from the list
                print("Item is removed from the list")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        openFile = open(objFile, "w")  # Opening the file in write mode
        for row in lstTable:  # Iterating through the list
            openFile.write(row['Task'] + ',' + row['Priority'] + '\n')  # Writing the data row by row in the file
        openFile.close()
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Exiting from the program")
        break
