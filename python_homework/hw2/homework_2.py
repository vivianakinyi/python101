## Defining a function
"""Transform your rock paper scissors program to a function """

# Math module
"""A module is a Python file with a collection of related functions. To use the module, you need to add the following line at the top of your
program, right underneath the comments with your name:
"""
import math

# print dir(math) # To see the functions in the math module

print 'Factorial', math.factorial(12)
print 'Squaroot', math.sqrt(49)


## Random module
import random
print random.randint(1, 100) # prints a random number btw 1 and 100

# To print 10 random numbers btw 1 and 100
print "10 random numbers btw 1 and 100"
for x in range(10):
	print random.randint(1,100)

# To print random multiple of 5 btw 1 and 100
print "random multiple of 5 btw 1 and 100"
for y in range(10):
	print random.randint(1,20)*5

#randrange : randrange ([start,] stop [,step])
# Select an even number in 10 <= number < 100
print "randrange(10, 100, 2) : ", random.randrange(10, 100, 2)

#Game of roll a dice
def roll_dice(sides, rolls):
	for x in range(rolls):
		roll_value = random.randint(1, sides)
		return roll_value

print "roll the dice", roll_dice(4, 3)
