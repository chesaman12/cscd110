def main():



    looping()

def print_it():
    print('''
    1. Anagram (Jumble) Solver
    2. Crossword Solver
    3. Scrabble Finder
    4. Palindrome Finder

    0. Exit

     ''')

def openfile():
    f = open('file.txt', 'r')
    filedata = f.readlines()
    f.close()
    i = 0
    for j in filedata:
        filedata[i] = j.strip()
        i += 1
    aDict = { 'file' : filedata }
    return aDict

def looping():
    print_it()
    dictionary = openfile()
    while True:
        ui = userInput()
        if ui == 1:
            is_anagram()
        #elif ui == 2:
        #elif ui == 3:
        elif ui == 4:
            userinput = int(input("Enter length of palindrome you would like to enter: "))
            for word in dictionary:
                is_palindrome(word)
        elif ui == 0:
            break

def  userInput():
    ui = int(input("What option would you like? "))
    return ui

def is_anagram(str1, str2):


def is_palindrome(word):
        if len(word) == ui and word == word[::-1]:
            return True
        else:
            return print("not valid")

main()