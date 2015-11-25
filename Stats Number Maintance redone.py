#Nate Elliott 11/14/15 Stats Number Maintance

def main():

   tryIt(looping())


def ui():
    printNumbers()
    userInput = int(input("What would you like to do? "))
    if userInput >= 7:
        print("Not an option")
        return -1
    else:
        return userInput



def looping():
    statsList = []
    while True:
        userInput = ui()
        if userInput == 1:
            addValue(statsList)
        elif userInput == 2:
            deleteValue(statsList)
        elif userInput == 3:
            deleteLocation(statsList)
        elif userInput == 4:
            displayList(statsList)
        elif userInput == 5:
            writeFile(statsList)
        elif userInput == 6:
           readFile(statsList)
        elif userInput == 0:
            break
        statsList.sort()




def addValue(statsList):
    
    ui = float(input("Enter number you'd like to add: "))
    statsList.append(ui)
    print("")

def deleteValue(statsList):

    ui = float(input("Enter number you'd like to remove: "))
    statsList.remove(ui)
    print("")

def deleteLocation(statsList):
    try:
        ui = int(input("Enter location you'd like to remove: "))
        statsList.pop(ui - 1)
    except IndexError:
        print("")
        print("Your list is empty!")
        return -1



def tryIt(MethodToRun):
    result = MethodToRun()
    try result:
        return result
    except KeyboardInterrupt:
        print("")
        print("Let the program do it's thing!")
        return -1



def printNumbers():
    print("Enter an option as an integer")
    print("1. Add Value to List")
    print("2. Delete Value from List (by value)")
    print("3. Delete Value from List (by location in list)")
    print("4. Display List with Location(s) within list")
    print("5. Read Values from File: numbers.txt")
    print("6. Write Values to File: numbers.txt")
    print("")
    print("0. Exit")
    print("")


def displayList(list):
    for idx, val in enumerate(list):
        print(str(idx+1) + " -> " + str(val))


def writeFile(statsList):
    fh = open("numbers.txt", "w")
    ui = int(input("Enter number you'd like to add to file: "))
    statsList.append(ui)
    fh.close

def readFile(list):
    fh = open("numbers.txt", "r")
    for idx, val in enumerate(list):
        print(str(idx+1) + " -> " + str(val))
    fh.close



main()