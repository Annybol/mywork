# randomfruit2.py
# using tuple this program prints out a random fruit
# Anne Boland

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear')


index = random.randint(0, len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))

