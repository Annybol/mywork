#convert.py
#takes a float and takes in a $amount and returns it in cents
#Anne Boland

import math
dollaramount = float(input("Enter a dollar: "))
cents = int(abs(dollaramount*100))
print ("cent amount is: " ,cents)
