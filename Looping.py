print("#1")
number1 = 33
while number1 >= 33 and number1 <= 36:
    number1 = number1 + 1
    print("\t",number1)

print("#2")
name = "Nate"
for letter in name:
    print("\t",letter)

print("#3")
number2 = 101
while number2 <= 101 and number2 >= 94:
    number2 = number2 - 1
    print("\t",number2)

print("#4")
number3 = 65
for number3 in range(65,59,-1):
    print("\t",number3)

print("#5")
number4 = 77
while number4 > 76 and number4 < 89:
    if number4 % 3 == 0:
        print("\t",number4)
    number4 = number4 + 1

print("#6")
number5 = 31
for number5 in range(31,2,-7):
    print("\t",number5)

print("#7")
number6 = 1
while number6 >= 1 and number6 <= 100:
    if number6 % 2 == 0 and number6 % 7 == 0:
        print("\t",number6)
    number6 = number6 + 1

print("#8")
number7 = 400
for number7 in range(400,199,-1):
    if number7 % 2 != 0 and number7 % 3 ==0 and number7 % 5 == 0:
        print("\t",number7)
