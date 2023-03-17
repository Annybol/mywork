# Creating a que of random numbers in a list
# Anne Boland 

import random
queue = []
numberOfNumber = 10
rangeTo=100

for n in range(0,numberOfNumber):
    queue.append(random.randint(0,rangeTo))

print (f"queue is {queue}")

while len(queue) !=0:

    currentNumber = queue.pop(0)
    #intructor omitted the 'f' in the following two commands and this was the ans to the q.
print(f"current Number is {currentNumber} and the queue is {queue} ")
print (f"the queue is now empty")