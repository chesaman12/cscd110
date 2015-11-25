#Nate Elliott 11/14/15 Stats Number Maintance
def main():
    print(printNumbers())
    looping()


def ui():
    userInput = int(input("What would you like to do? "))
    if userInput >= 7:
        print("Not an option")
        return -1
    else:
        return userInput



def looping():
    while True:
        ui == ui()
        if ui == 1:
            addValue()
        #elif ui == 2:
        #    function
        #elif ui == 3:
        #    function
        #elif ui == 4:
        #    function
        #elif ui == 5:
        #    funcion
        #elif ui == 6:
        #   function
        elif ui == 0:
            break


def uiadd():
    uia = float(input("What number would you like to add?"))
    return uia


def addValue(uia):
    list.append(uia)

#def tryIt(function):
#   try function:
#        return function
#    except KeyboardInterrupt:
#        print("")
#        print("Let the program do it's thing!")
#        return -1



def printNumbers():
    print("Enter an option as an integer")
    print("1. Add Value to List")
    print("2. Delete Value from List (by value)")
    print("3. Delete Value from List (by location in list)")
    print("4. Display List with Location(s) within list")
    print("5. Read Values from File: “numbers.txt”")
    print("6. Write Values to File: “numbers.txt”")
    print("")
    print("0. Exit")






main()
