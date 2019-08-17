'''
This is a tutorial for python 101
'''
print "Hello world"

#This is a comment

'''
This is a multi-line comment
'''

# STRINGS
# Strings are datatype rep letters, numbers or special characters rep in double/single quotes

print "This is a string"


# VARIABLES
# Variables are a store of value
name = "Vivian"
print "Hello ", name

first_name = "Vivian"
second_name = 'Omondi'

print "My first name is " , first_name + ' and second name ' + second_name

# DATA TYPES (numbers, strings, dictionaries, list, tuples)

# There are 7 diff arimethic operators + - * / % ** //

print "5 + 2 = ", 5+2
print "5 - 2 = ", 5-2 
print "5 * 2 = ", 5*2
print "5 / 2 = ", 5 / 2.0
print "5 // 2 = ", 5//2.0  # truncates
print "5 ** 2 = ", 5**2 # power
print "5 % 2 = ", 5%2  # modulus/reminder

# Note:Order of operation matters
print "1 + 2 - 3 * 2 = ", 1 + 2 - 3 * 2
print "(1 + 2 - 3) * 2 = ", (1 + 2 - 3) * 2

# LIST : Similar to arrays. Contains any data type with first index as 0
shoppingList = []
shoppingList.append("tomatoes")
shoppingList.append("bread")
shoppingList.append("tissue")
shoppingList.append("pens")


print shoppingList
print shoppingList[0]
print shoppingList[2]

# Get lenghth of list
print len(shoppingList)

#Delete an item
# del shoppingList[1]
# print shoppingList

#Sort list
numlist = [4,3,2,1]
print sorted(numlist)

#Slice
print shoppingList[1:3]

# Combine lists
print shoppingList.append(numlist)

new_list = shoppingList + numlist
print new_list

# TUPLES:  IMMUTABLE cant be changed once created. Rep in ()
my_tuple = (2,3,4,17,9)
# my_tuple.append(12) # Tuple is Immutable (cant be changed)
print my_tuple

print len(my_tuple)
print my_tuple[4]
print my_tuple[1:4] # slice
print max(my_tuple)
print min(my_tuple)

# convert tuple to list 
tuple_to_list  =  list(my_tuple)
print "convert tuple to list", tuple_to_list

# convert list to tuple
list_to_tuple = tuple(tuple_to_list)
print "convert list to tuple", list_to_tuple

# DICTIONARY : values with unique key
student_details = {'id':1234, 
					"name":"Derick Mwenda", 
					'course':'computer science',
					'year' : 3 }

print student_details

# Access values using the keys
print 'ID ',student_details['id']
print 'name ', student_details['name']

# Updating a dictionary key-value
student_details['course'] = 'Software Eng'
student_details['unit'] = "Data structures"
print 'New details ',student_details

# Delete 
del student_details['unit'] # remove entry witth key unit
print student_details

# student_details.clear() # removes all entries in a dict
# print student_details

# del student_details # delete entire dict
# print student_details

# Built in functions
print 'length = ',len(student_details) # length of string
print 'string ',str(student_details) #string represnation of a dict
print 'Keys ',student_details.keys() 
print 'Get value ', student_details.get('name')
print 'key, value tuple ', student_details.items() 
print 'Values ', student_details.values()

print 'Has key course?  ',student_details.has_key('course') 
print 'Has key unit?  ',student_details.has_key('unit') 

# looping 
for key in student_details:
	print key

for key, val in student_details.items():
	print key, val

# CONDITIONALS if else elif
age = 5

if age < 18 and age != 18:
	print "Cannot vote"
elif age >= 18 or age == 18:
	print 'Can vote'
else:
	print 'Invalid'

# FOR Loop
for x in range(0,10):
	print x

for y in shoppingList:
	print y

for z in [10,201,20,50]:
	print z

# Functions: Block of reusable code defined using keyword def. Note the indentation after colon :
def sum(arg1, arg2):
	total = arg1 + arg2
	print "Sum of ", arg1, ' + ', arg2, ' = ', total
	return 

# Calling the function with paramenters/arguments
sum(10,50)






