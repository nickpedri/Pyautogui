#  Putting a '#' on a line will turn it into a comment. Comments do not affect code
#  A comment is like a note
#  Hi my love <3
#  Thank you for agreeing to this
# i want to kiss you

# -------------------------------------------
#  1. Learning what variables are

variable = 'A variable is symbolic name that holds a value!'
name2 = 'nick'  # String
last_name2 = 'pedri'  # String
age2 = 28  # Integer (number)
hobbies2 = ['games', 'woodworking', 'gym']  # List
pregnant2 = False  # Boolean (True or False)
dictionary2 = {'key': 'value'}  # dictionary

# Put Nelly's info under here

name = 'fatty'
last_name = 'pedri'
age = 4
hobbies = ['snuggles', 'naps', 'eating']
cat = True

# --------------------------------------
#  2. Using print statements

#print('You can use print() to make Python write out what you want.')
"""
print(name)
print(last_name)
print(name, last_name)
print(age)
print(hobbies)
print(cat)
print()
"""

# --------------------------------------
#  3. Types of data
#  There are different types of variable in Python

#  Use type() to check the type of data
def hide():
    a = type(name)
    print(a)
    print(type(age))
    print(type(hobbies))
    print(type(cat))

    numbers = range(1, 31)  # The second number of a range is exclusive meaning it is not included. 10 will not be included
    print(numbers)
    print(type(numbers))
    print(list(numbers))


# --------------------------------------
#  4. Basic loops

# You can use loops to iterate through lists, ranges, strings,
variable = [name, last_name, age, hobbies, cat]  # reassign variable
numbers = [1, 2, 3, 4, 5, 10]  # Create list of numbers
names = ['nick', 'nelly', 'fatty', 'vanessa']
random = ['string', 7, True, []]


for rrrrr in random:
    #print(type(rrrrr))
    #print(rrrrr)
    pass


for numb in numbers:
    #print(numb)
    #print(type(numb))
    #print('hi')
    pass


for v in variable:
    #print(v)
    #print(type(v))
    pass


for n in names:
    #print(n)
    pass

# --------------------------------------
#  5. Creating functions
#  You can create your functions by using 'def ' followed by the name of your function


def example():
    print('This is an example of a function!')
    print('You can make a function as simple or as complicated as you want.')
    print('They are useful when performing actions repeatedly.')
    print('With this basic function I can print 4 lines with one function call.')


#example()


def print_hello(x):
    """This function takes in an integer (number) x and prints out hello x amount of times"""
    x = range(1, x+1)  # convert x into a range of numbers
    for num in x:  # Use for loop to iterate through x
        print('hello')  # Each loop will print out hello
        #print(num)


print_hello(0)


# --------------------------------------
#  6. IF statements  &  equality operators
# you can use equality operators to yield true or false from them
# an IF statement will run the code below it if the condition that follows it is true

if True:
    pass
    #print(True)

if False:
    print(False)

#   ==  checks if the values are equal
#   !=  checks if the values are not equal
#   >   (Greater than)
#   <   (Less than)
#   >=  (Greater than or equal to)
#   <=  (Less than or equal to)


def equality_examples():
    print('5 == 6 is: ', 5 == 6)
    print('5 != 6 is: ', 5 != 6)
    print('5 > 6 is: ', 5 > 6)
    print('5 < 6 is: ', 5 < 6)


# equality_examples()

# we can combine functions with equality operators to create some usable python logic


def is_number_below_ten(x):
    if x < 10:
        print(f'Number {x} is below ten!')
    else:  # you can pair an IF STATEMENT with an ELSE STATEMENT that will execute if the IF STATEMENT is false
        print(f'Number {x} is NOT below ten!')


# is_number_below_ten(12)


# --------------------------------------
#  7. Dictionaries
# A dictionary is a type of data that stores data in key:value pairs
# It can make storing data easier, especially if data pertains to a similar 'category'

nick = {
        'name': 'nick',
        'last_name': 'pedri',
        'age': 28,
        'hobbies': ['games', 'woodworking', 'gym'],
        'pregnant': False,
        'loves_wife': True
       }

# print(nick)

for i in nick:
    # print(i, ': ', nick[i])
    pass


def display_info(person):
    for item in person:
        print(item, ': ', person[item])


# display_info(nick)
