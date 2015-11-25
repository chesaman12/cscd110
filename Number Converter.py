def main():
    looping()
def looping():
    l = []
    while True:
        ui = userInput()
        if ui == 1 or 2 or 3:
            number = inputNum()
            l.append(number)
        elif ui == 4:
            decobin(l,2) and decobin(l,10) and decobin(l,16)
        elif ui == 0:
            break





def  userInput():
    printit()
    ui = int(input("What option would you like?"))
    return ui

def inputNum():
    ui = int(input("Enter Number: "))
    return ui
def printit():
    print('''
    1. Enter number in decimal
    2. Enter number in hexidecimal
    3. Enter number in binary
    4. Display number in Decimal, Hexadecimal, and Binary

    0. Exit
    ''')

def decobin(num, base):
    num = list(map(int, num))
    result = ""
    while num > 0:
        bit = num % base
        if bit == 10:
            result = "A" + result
        elif bit == 11:
            result = "B" + result
        elif bit == 12:
            result = "C" + result
        elif bit == 13:
            result = "D" + result
        elif bit == 14:
            result = "E" + result
        elif bit == 15:
            result = "F" + result
        elif bit == 16:
            result = "G" + result
        else:
            result = str(bit) + result
        num = num // base
    print(result)

main()

