def main():
    a()
    
def base():
    base = int(input("Enter base you are converting to: "))
    return base

def decimal():
    decimal = int(input("Enter number you are converting: "))
    return decimal

def result():
    result = ""
    return result

def a():
    while decimal() > 0:
        bit = base() % decimal()
