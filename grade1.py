# grade1.py
# same as grade.py with the modification to round 69.5 to 70 
# Anne Boland 

percentage = float (input("Enter the percentage: "))
# print percentage
# be careful with ands and ors
if percentage < 0 or percentage >100:
    print ("Please enter a number bewtwwn 0 and 100")


elif percentage < 40: 
    print ("Fail")
elif percentage < 50:
    print ("pass")
elif percentage < 60:
    print ("Merit 1")
#modification to raise 69.5-69.9 to 70% changed <70 to <69.5
 
elif percentage < 69.5: 
    print ("Merit 2")
else:
    print ("Distinction")
