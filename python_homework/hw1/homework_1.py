""" Write a program using a while loop that asks the user for a number, and prints a countdown from that number
to zero. What should your program do if the user inputs a negative number? As a programmer, you should
always consider 'edge conditions' like these when you program! (Another way to put it- always assume the
users of your program will be trying to find a way to break it! If you dont include a condition that catches
negative numbers, what will your program do?) """

num = input("Enter a number ")
if num < 0 :
	print "Only positive numbers allowed"

else:
	for x in range(num, 0, -1):
		print x

"""Write a program using a for loop that calculates exponentials. Your program should ask the user for a base
base and an exponent exp, and calculate base^exp
"""
base = input("Enter the base ")
for exp in [2,3,4]:
	print base^exp


"""  Write a program using a while loop that asks the user to enter a number that is divisible by 2. Give the user
a witty message if they enter something that is not divisible by 2- and make them enter a new number. Don’t
let them stop until they enter an even number! Print a congratulatory message when they *finally* get it
right."""
