Hole = int(input("Enter the hole number: ")) #Asks the user for the hole number
Par = int(input("Enter the par for the hole: ")) #Asks the user for the par of the hole
Strokes = int(input("Enter the number of strokes: ")) #Asks the user for how many strokes it took

realPar = Strokes - Par #Subtracts the strokes and par to get what the users par was

if realPar == -5: #This if statement sets a variable to a string depending on the value of the users par
    ParName = "you hit an ostrich"
elif realPar == -4:
        ParName = "you shot a condor"
elif realPar == -3:
        ParName = "you shot an albatross"
elif realPar == -2:
        ParName = "you shot an eagle"
elif realPar == -1:
        ParName = "you shot a birdie"
elif realPar == -0:
        ParName = "you shot an even Par"
elif realPar == 1:
        ParName = "you shot a bogey"
elif realPar == 2:
        ParName = "you shot a double Bogey"
elif realPar == 3:
        ParName = "you shot a triple Bogey"
else:
        ParName = (("you shot a {} over par").format(realPar))

if Strokes == Par*2: #This if statement sets a variable to a string only if the users stroke amount was twice that of the holes par
    Beagle = ", a damned Beagle"
else:
    Beagle = ""

if Strokes == 1: #This if statement sets a variable to a string only if the users strokes = 1,4,8 or 10
    ActualParName = ", with a hole in one"
elif Strokes == 4:
    ActualParName =", with a sailboat"
elif Strokes == 8:
    ActualParName =", with a snowman"
elif Strokes == 10:
    ActualParName =", with a Bo Derek"
else:
    ActualParName = ""

if Strokes in [1,4,8,10] or Beagle != "": #This if statement is just for sytntax in the final print statement
    Punc = "!" #The program will  look for the stroke value and if its 1,4,8,10 or a beagle then a variable will be set an !
else: #If it isn't one of the values listed then it will just set the variable to a .
    Punc = "."

print(("On hole #{0} a par {4} {1}{2}{3}{5}").format(Hole, ParName, ActualParName, Beagle, Par, Punc)) #The final print statement
