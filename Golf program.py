Hole = int(input("Enter the hole number: "))
Par = int(input("Enter the par for the hole: "))
Strokes = int(input("Enter the number of strokes: "))

realPar = Strokes - Par

if realPar == -5:
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

if Strokes == Par*2:
    Beagle = ", a damned Beagle"
else:
    Beagle = ""

if Strokes == 1:
    ActualParName = ", with a hole in one"
elif Strokes == 4:
    ActualParName =", with a sailboat"
elif Strokes == 8:
    ActualParName =", with a snowman"
elif Strokes == 10:
    ActualParName =", with a Bo Derek"
else:
    ActualParName = ""

if Strokes in [1,4,8,10] or Beagle != "":
    Punc = "!"
else:
    Punc = "."

print(("On hole #{0} a par {4} {1}{2}{3}{5}").format(Hole, ParName, ActualParName, Beagle, Par, Punc))
