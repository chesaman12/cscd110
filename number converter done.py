import logging, sys
#note, turn this to INFO before turning in
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

def main():
    looping()
def looping():
    number = -1
    while True:
        ui = userInput()
        if ui == 1:
            number = inputNum()
            is_base(number)
        elif ui == 2:
            number = is_hex()
        elif ui == 3:
            num = inputNum()
            number = is_binary(num)
        elif ui == 4:
            decobin(number,2)
            decobin(number,10)
            decobin(number,16)
        elif ui == 0:
            break

def  userInput():
    printit()
    ui = int(input("What option would you like? "))
    return ui

def inputNum():
    try:
        ui = int(input("Enter Number: "))
        return ui
    except ValueError:
        print("Enter an integer please!")
        return -1
    except KeyboardInterrupt:
        print("Let the program do it's thing!")
        return -1

def is_binary(num):
    for digit in str(num):
        if digit != "0" and digit != "1":
            print("Not in binary")
            return False
        return binodec(num)

def is_hex():
    ui = input("Enter a number in hex: ")
    for digit in ui:
        if digit not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
            print("Not in hexadecimal")
            return False
    return hexodec(ui)

def is_base(ui):

    for digit in str(ui):
        if digit not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Not in decimal!")
            return False
    return True

def printit():
    print('''
    1. Enter number in decimal
    2. Enter number in hexidecimal
    3. Enter number in binary
    4. Display number in Decimal, Hexadecimal, and Binary

    0. Exit
    ''')

def decobin(num, base):
    logging.debug("num -> " + str(num))
    logging.debug("base -> " + str(base))

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
        else:
            result = str(bit) + result
        num = num // base
    print("base ->",str(base),"number ->", result)


def hexodec(num):
    digit = int(num,16)
    return digit

def binodec(num):
    dec = str(num)
    digit = int(dec, 2)
    return digit
    


main()

