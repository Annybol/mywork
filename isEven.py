#isEven.py
#Asks to enter in a number and program tells the user if the number is odd or even
# Anne Boland

number = int(input("enter an integer: "))

# NB-Dont forget the colons after command on if and else
if (number/2) == (0):
    print (f"{number} is an even number")
else:
    print (f"{number} is an odd number")
