#collat.py 
#maths problem how every number can end up with the answer one depanding on odd even
# Anne Boland

number = int(input("Enter any number:"))

if number%2 == 0:
     print(f"{(number/2)}")
else: 
    print(f"{(number*3)+1}")
