#this program returns if a day of the week is a weekday or weekend using dictionary
#Author: Anne Boland 


Weekday = {
        "Monday": "Yes, unfortunately today is a weekday",
        "Tuesday" :"Yes, unfortunately today is a weekday",
        "Wednesday":"Yes, unfortunately today is a weekday",
        "Thursday":"Yes, unfortunately today is a weekday" ,
        "Friday":"Yes, unfortunately today is a weekday",
        "Saturday":"Yay, its the weekend",
        "Sunday":"Yay, its the weekend" 
}
attr = (input("Enter any day:"))
# must be a better way to assign similar values.
# Ref from Python code and W3Schools and attr from online lecture

print (Weekday[attr])

