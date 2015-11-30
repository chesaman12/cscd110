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

def looping():
    dictionary = openfile()
    while True:
        print_it()
        ui = userInput("What option would you like? ")
        if ui == 1:
            userinput = input("Enter letters for anagram: ")
            for word in dictionary:
                if is_anagram(word,userinput):
                    print(word)
        elif ui == 2:
            userinput = input("Enter letters for crossword, ? means space: ")
            for word in dictionary:
                if is_crossword(word,userinput):
                    print(word)
        elif ui == 3:
            userinput = input("Enter letters for scrabble: ")
            for word in dictionary:
                if is_scrabble(word,userinput):
                    print(word, scrabblewordscore(word))
        elif ui == 4:
            userinput = userInput("Enter length of palindrome you would like to enter: ")
            for word in dictionary:
                if is_palindrome(word,userinput):
                    print(word)
        elif ui == 0:
            break

def  userInput(prompt):
    ui = int(input(prompt))
    return ui

def is_anagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return str1_list == str2_list

def is_palindrome(word,ui):
        if len(word) == ui and word == word[::-1]:
            return True
        else:
            return False

#new comment
def is_crossword(word, pattern):
    if len(word) == len(pattern):
        pos = 0
        x = 1
        for letter in pattern:
            if not letter == "?":
                if not letter == word[pos]:
                    x = 0
                pos += 1
            if x == 1:
               return True

def is_scrabble(tiles,word):


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
            val += "10"
    return val



main()