a = int(input("Please enter the value of a " ""))
b = int(input("Please enter the sign of b " ""))
c = int(input("Please enter the value of c " ""))

if (b <= a <= c) or (c <= a <= b):
    print("The median is", a)
elif (a <= b <= c) or (c <= b <= a):
    print("The median is ",b)
else:
    print("The median is", c)