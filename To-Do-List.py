#Matthew Allicock
#100860998

import datetime


def addNewItems():
    global ToDoList
    taskA = input('Enter the name of the task A: ')
    date_time = input(
        "Enter the task completion date (yyyy/mm/dd HH:MM:SS) : ")
    datetime_obj = datetime.datetime.strptime(date_time, '%Y/%m/%d %H:%M:%S')
    if datetime_obj < datetime.datetime.now():
        print('Time entered is in the past! Select the options again')
        return
    if checkItemExists(taskA):
        print('Task already exists! Select the options again')
        return
    ToDoList.append((taskA, datetime_obj))
    print('Task added successfully!')
    ToDoList.sort(key=takeSecond)
    return

def checkItemExists(taskName):

    global ToDoList
    for task in ToDoList:
        if taskName == task[0]:
            return True
    return False

def takeSecond(element):
    return element[1]

def printListItems():
    global ToDoList
    print('')
    for ind, task in enumerate(ToDoList):
        print(f"{ind}. {task[1]} - {task[0]}")
    return

def removeListItems():
    global ToDoList
    delete = int(input('Enter which task would you like to delete [select Tasks starting from 0] : '))
    del ToDoList[delete]
    print('Task deleted successfully')

ToDoList = []

while True:

    print('1. Enter a new To do item')
    print('2. Print the list of all To do items')
    print('3. Remove a To do item')
    print('4. exit the program')
    options = int(input('Enter a choice : '))

    if options == 1:
        addNewItems()
    elif options == 2:
        printListItems()
    elif options == 3:
        removeListItems()

    elif options == 4:
        print('End of program')
        break
