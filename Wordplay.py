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

def looping():
    while True:
        ui = userInput()
        if ui == 1:
            is_anagram()
        #elif ui == 2:
        #elif ui == 3:
        elif ui == 4:
            is_palindrome()
        elif ui == 0:
            break

def  userInput():
    print_it()
    ui = int(input("What option would you like? "))
    return ui

def is_anagram():
    return  True

def is_palindrome():




main()