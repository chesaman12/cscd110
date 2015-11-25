startnum = int(input("Enter starting value: "))
endnum = int(input("Enter ending value: "))
z = 0
y = 1
t = 0

for numbers in range(startnum,endnum+1,1):
    for a in str(numbers):
        z = z + int(a)
    for b in str(numbers):
        y = y * int(b)
    t = t + y
    y = 1
print("Digit sum:",z)
print("Digit product:",t)
        
        
    
