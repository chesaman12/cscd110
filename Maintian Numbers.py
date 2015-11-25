#Nate Elliott 11/7/15 Maintain Numbers
def main():

   inputLooping()
  
def inputLooping():
    try:
        while True:
             userInput = inputFromUser()
             if userInput == 1:
                 addNumber()
             elif userInput == 2:
                 removeNumber()
             elif userInput == 3:
                 removeNumberList()
             elif userInput == 4:
                 displayList()
             elif userInput == 0:
                 print("Goodbye!")
                 break
    except KeyboardInterrupt:
        print("")
        print("Let the program do it's thing!")
        return -1
                 
           
def inputFromUser():
    try:
            print("1 - add number to file")
            print("2 - remove number from file")
            print("3 - remove number by place in list")
            print("4 - display list")
            print("")
            print("0 - exit")
            print("")
            userInput = int(input("What would you like to do? "))
            if userInput >= 5:
                print("Not an option")
                return -1
            else:
                return userInput


    except ValueError:
        print("Enter an integer please!")
        return -1
       
    except KeyboardInterrupt:
        print("Don't interrupt during program please!")
        return -1


def addNumber():
    try:
        fh = open("numbers.txt","a")
   
        intNum1 = int(input("Enter number you would like to add to file: "))
        strNum1 = str(intNum1)
        strNum2 = strNum1 + "\n"
        fh.write(strNum2)
        fh.close()

    except ValueError:
        print("Enter an integer please!")
        return addNumber()
    except KeyboardInterrupt:
        print("Don't interrupt during program please!")
        return addNumber()   
    
def removeNumber():
    try:
        x = int(input("What number would you like to remove? "))
        y = str(x)
        fh = open("numbers.txt","r")
        lines = fh.readlines()
        fh.close()
        f = open("temp.txt","w+")
        found = False
        for line in lines:
            line = line.strip() 
            if line == y and not found:
                found = True
            else:
                f.write(line + "\n")
        #if found == False and f.readlines() == 0:
        #    print("You're file is empty! Try adding numbers with option 1")
        #    return -1
        if found == False:
            print("That isn't a number in the file, check the display if needed (option 4)")
            return -1
        f.close()
        #fh.close()
        fh = open("numbers.txt","w")
        f = open("temp.txt","r")
        lines = f.readlines()
        for line in lines:
            fh.write(line)
        fh.close()
        f.close()
    except ValueError:
        print("Enter an integer please!")
        return removeNumber()
    except KeyboardInterrupt:
        print("Don't interrupt during program please!")
        return removeNumber()
              

def removeNumberList():
    try:
        fh = open("numbers.txt","r")
        lines = fh.readlines()
        fh.close()

    
        ui = int(input("What line would you like to delete? "))
    
        fh = open("temp.txt","w")
        linenumber = 1
        for line in lines:      
            if linenumber != ui:
                  fh.write(line)
            linenumber += 1
        if linenumber <= ui:
            print("There isn't a number on that line, check the display if needed (option 4)")
            return -1
        fh.close()
        fh = open("numbers.txt","w")
        f = open("temp.txt","r")
        lines = f.readlines()
        for line in lines:
            fh.write(line)
        fh.close()
        f.close()
    except ValueError:
        print("Enter an integer please!")
        return removeNumberList()
    except KeyboardInterrupt:
        print("Don't interrupt during program please!")
        return removeNumberList()

def displayList():
    try:
        fh = open("numbers.txt","r")
        linenumber = 1
        Peroid = "."
        print("List of numbers from file")
        for number in fh:
            print("{0}{1} {2}".format(linenumber, Peroid, number.strip()))
            linenumber += 1
        fh.close()
    except KeyboardInterrupt:
        print("")
        print("Stop pressing ctrl + c!")
        print("")
        return displayList()
    
    except ValueError:
        print("")
        print("Buttons are not needed right now")
        return displayList()
   
main()

        
