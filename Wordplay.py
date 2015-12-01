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
    return filedata

#comment
def looping():
    dictionary = openfile()
    while True:
        print_it()
        ui = userInput("What option would you like? ")
        if ui == 1:
            try:
                userinput = input("Enter letters for anagram: ")
            except:
                print("Not valid")
                return -1
            for word in dictionary:
                if is_anagram(word,userinput):
                    print(word)
        elif ui == 2:
            try:
                userinput = input("Enter letters for crossword, ? means space: ")
            except:
                print("Not valid")
                return -1
            for word in dictionary:
                if is_crossword(word,userinput):
                    print(word)
        elif ui == 3:
            try:
                userinput = input("Enter letters for scrabble: ")
            except:
                print("Not valid")
                return -1
            for word in dictionary:
                if is_scrabble(word,userinput):
                    print(word)
        elif ui == 4:
            userinput = userInput("Enter length of palindrome you would like to enter: ")
            for word in dictionary:
                if is_palindrome(word,userinput):
                    print(word)
        elif ui == 0:
            print("Goodbye!")
            break

def  userInput(prompt):
    try:
        ui = int(input(prompt))
        return ui
    except:
            print("Not valid")
            return -1

def is_anagram(str1, str2):
    strList1 = list(str1)
    strList1.sort()
    strList2 = list(str2)
    strList2.sort()

    return strList1 == strList2

def is_palindrome(word,ui):
        if len(word) == ui and word == word[::-1]:
            return True
        else:
            return False

def is_crossword(word, pattern):
    if len(word.lower()) == len(pattern.lower()):
        for i,letter in enumerate(pattern.lower()):
            if not letter == "?":
                if not letter == word[i]:
                   return False
            return True

def is_scrabble(tiles,word):
    tl = list(tiles.lower()) #makes the tiles a list)
    for letter in word.lower(): #for each letter in the word
        if letter in tl: #if the letter is in the tiles then continue
            tl.remove(letter) #remove that letter
        else:
            return False #if any part does not pass then the word wont be displayed
    return True #if all parts passed then the word will be displayed

def scrabblewordscore(word):
    val = 0
    for ch in word:
        if ch in "aeioulnstr":
            val += 1
        elif ch in "dg":
            val += 2
        elif ch in "bcmp":
            val += 3
        elif ch in "fhvwy":
            val += 4
        elif ch in "k":
            val += 5
        elif ch in "jx":
            val += 8
        elif ch in "qz":
            val += 10
    return val



main()