name = input("Enter your name: ") #Asks the user for their name
snum1 = input("Enter number of T-shirts sold: ") #Asks the user for number of shirts
snum2 = input("Enter cost per shirt: ") #Asks the user for cost per shirt

num1 = float(snum1) #changes the type str to type float for snum 1
num2 = float(snum2) #changes the type str to type float for snum 2

amt = float(num1 * num2) #multiply's num1 and num 2

print("") #Puts a blank line between user inputs and program outputs

print("---"+ name + "'s","Receipt---") #Prints name and receipt
print("Quanity of T-shirts:",format(num1,",.0f")) #Prints quantity of shirts
print("Price per shirt:","$"+format(num2,",.2f")) #Prints price per shirt
print("Total price:","$"+format(amt,",.2f")) #prints a $ and formats the float to have 2 decimals, thus displaying the final cost
