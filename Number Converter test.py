def main():
    decobin(234,16)
def decobin(num, base):

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

