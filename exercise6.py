x = int(input("Please enter the value of x " ""))
y = int(input("Please enter the value of y " ""))
z = int(input("Please enter the value of z " ""))

if x == y and y == z:
    print("There are three matches")
elif x == y or x == z or y == z:
    print("There are two matches")
else:
    print("There is only one match")
    