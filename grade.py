# grade.py
# reads students percentage and prints a corresponding grade
# Anne Boland 

percentage = float (input("Enter the percentage: "))
# print percentage
# be careful with ands and ors
if percentage < 0 or percentage >100:
    print ("Please enter a number between 0 and 100")

elif percentage < 40: 
    print ("Fail")
elif percentage < 50:
    print ("pass")
elif percentage < 60:
    print ("Merit 1")
elif percentage < 70: 
    print ("Merit 2")
else:
    print ("Distinction")
