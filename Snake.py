#dec = int(input("Number in base 10:" ))
dec = 4537
result = ""
base = 2

while dec > 0:
    bit = dec % base
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
        result = str(bit)
    dec = dec // base
    print(result )
