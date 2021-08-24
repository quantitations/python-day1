

##################### CALCULATIONS ##################

4+5
4 + 5
4+  5
# Python doesn't seem to care about spacing...
# This is true to an extent within a command but BEWARE
# - PRECISE INDENTING is CRUCIAL as we'll see later

4 * 3
2 + 4 * 3
(2 + 4) * 3

4 / 3
4 % 3

4**2
4^2
# This doesn't cause an error - it appears to add the numbers...
# It would be easy to accidentally use this and never realize your mistake


## EXERCISE 1: Use Python to calculate the length of the hypotenuse of
##             a right triangle whose other two sides have lengths 1 and 4.
##             (Remember Pythagorean Theorem: it's the square root of 1 squared plus 4 squared)




################### DEFINING VARIABLES ######################

a = 36
b = 4
a*b



######################### STRINGS ##########################

print("Hi there.")

print('hi') # single quote symbol works too

h = "Hi there."

h + " How are you?"
h

"I'd like " + a + " eggs, please."
"I'd like " + str(a) + " eggs, please."
"I'd like %s eggs, please." % a
f"I'd like { a } eggs, please."
f"I'd like { a/12 } dozen eggs, please."

f = """Hi there.
How are you?"""
f
print(f)




########################## LISTS ###############################

d = [1, 2, a, b]
d
d[0]
d[1]
d[-1] # negative counts from the end
d[:2] # subset stopping BEFORE index 2
d[2:] # subset starting at index 2
d[1:3]

d + [5, 6] # concatenates - not like R vectors
d

d[1] = 4
d

d[2:] = [5, 6]
d

d.append(7)
d

len(d)

[4, h]
# A list can contain a combination of different types

[3, d] # this doesn't concatenate - not like R vectors
# A list can contain a list

h[3:]
h[3:-1]
# A strings can be subsetted as if it were a list of characters

# Except that you can't CHANGE the string in the same way
h[-1] = "!"

# You'd have to make a new string instead
h = h[:-1] + "!"
h

# WARNING !!!
d
c = d
c[0] = 0
c
d
# the names "c" and "d" both point to the same object
# to create "c" as a new object that is a copy of "d"
c = d.copy()
c[0] = 1
c
d
# ("dictionary" objects work like this too...)




########################### TUPLES ################################

# A tuple is like a "lightweight" list
# - computations with tuples are generally faster and less memory intensive
# - but tuples are less versatile

# use parentheses rather than square brackets
t = (1, 2, 8)
t

# or just separate the entries with commas
u = 4, 5, 9
u

# you can even use a tuple on both sides of the equal sign
# for entry-by-entry assignment
v, w, x = 3, ["hi", "there"], range(5)
v
w
x



# entries and subsets (just like lists)
u[0]
u[1:]

# changing a tuple?
u[0] = 1  # doesn't work! unlike lists

# can turn a tuple into a list
list(u)




########################### DICTIONARIES #######################

# a set of key-value pairs
d = {"name": "Jack", "height": 68}
d
d["name"]
d["height"] = 67
d["weight"] = 180
d
d.keys()
d.values()


people = [] # empty list
people.append(d) # in "in-place" operation
people


## EXERCISE 2: Create a "dictionary" object for Jill (whose height is 68 and
##             weight is 165) and append it to "people".







######################## CONDITIONALS ############################

b
b==4 # notice TWO equal signs rather than ONE
not b==4
not b>=5
b!=5

if b==4:
    print("YES, four")
    print(b)
# notice it's INDENTATION that defines the scope - no brackets needed

if not b==4:
    print("NO, not four")
else:
    print("YES, four")

if b==3:
    print("it's exactly three")
elif b > 3:
    print("it's greater than three")
else:
    print("it's less than three")

a

if a < 5 and b < 5:
    print("both are less than five")
elif a < 5 or b < 5:
    print("only one of them is less than five")
else:
    print("both are at least five")



###################### LOOPS #####################################

i = 1
while i <= 5:
    print(i)
    i = i+1

i = 1
while True:
    print(i)
    i+=1 # equivalent to "i = i+1"
    if i > 5:
        break

for j in [1, 4, 5]:
    print(j)

s = "I hope you're well"
s.split("e")
words = s.split() # splits at spaces and newlines by default
words

"I hope you're well\nor at least that you're getting better".split()

for w in words:
    print(w, len(w))
    
for w in words:
    if "'" in w:
        continue
    print(w)

for j in range(10):
    print(j)

for j in range(len(words)):
    print(j, words[j])

for j in range(1, 10): # if you want to start at 1 instead of 0
    print(j)

for j in range(0, 10, 2):
    print(j)

range(10) # not actually a list, only an "iterator", i.e. an instruction for constructing a list one item at a time
list(range(10))

# for loop over dictionary
d
for k in d:
    print(k, d[k])



### CONSTRUCT A LIST VIA A FOR LOOP, a.k.a. "LIST COMPREHENSION" ###

# Suppose you want to make a new list by doing the same thing to each entry of another list (or iterator).
# As a simple example, let's create a list of the squares of 1 through 10
squares = []
for i in range(1, 11):
    squares.append(i**2)
squares

# Python has a special shorthand notation for this type of task,
# with the for loop inside the list definition.
[i**2 for i in range(1, 11)]

# You can also add a conditional in order to only include a subset of the list.
# For example, here are the squares of the even numbers between 1 and 10.
[i**2 for i in range(1, 11) if i % 2 == 0]

# Realize that the this isn't limited to lists of numbers
greeting = "What are you going to do today"
# List of the words that start with "T" or "t"
[s for s in greeting.split() if s[0] in ["T", "t"]]
# Make them all-capitals
[s.upper() for s in greeting.split() if s[0] in ["T", "t"]]

# List comprehension isn't strictly necessary, but it does allow you to pack
# quite a bit of work in a single tidy line of code.


# EXERCISE 3: In a single line of code, create a list of the words in the
#             "greeting" string defined above that have at least four letters.
#             The words should be converted to all-lower-case letters.





############################## FUNCTIONS ###############################


def hello():
    print("Hello there!")
    
hello()

def hello(name="you"):
    print(f"Hello, { name }!")

hello()
hello("everybody")

students = ["Jim", "Joe", "Jane"]
for student in students:
    hello(student)

def sum_powers(v, p=1):
    powers = [i**p for i in v]
    return sum(powers)

sum_powers([1, 3, 5])
sum_powers([1, 3, 5], 2)
sum_powers(p=2, v=[1, 3, 5])

# here's a function that returns a tuple
def squareAndCube(x):
    return x**2, x**3

a, b = squareAndCube(3)
a
b

## EXERCISE 4: Write a function that takes as its parameters two sides of 
##             a right triangle and returns the length of the triangle's
##             hypotenuse. Use your function to find the length of the hypotenuse
##             if the other two sides have lengths 3 and 4.





############################### CLASSES ##############################

# By creating a class, you're able to define a new type of variable
# with its own properties and functions.

# Defining a class


class YaleCourse:

    def __init__(self, department, number, credits):
        self.department = department
        self.number = number
        self.credits = credits


# Creating instances of this class
c1 = YaleCourse("S&DS", 100, 3)
c2 = YaleCourse("S&DS", 312, 3)
# (If there is a function called __init__, it runs automatically
#  whenever a new instance of the class is created.
#  The "self" parameter refers to the specific instance at hand,
#  and it's passed into the function automatically.)

# The __init__ function created class properties for each YaleCourse instance that we defined.
# The properties can be accessed by instance-name dot property-name.
c1.number
c2.number


# Defining another class

class YaleStudent:

    def __init__(self, name):
        self.name = name
        self.courses = []
        self.credits = 0

    def courseComplete(self, course):
        self.courses.append(course)
        self.credits += course.credits


# Creating an instance of this class
s = YaleStudent("Jack")
s.credits

# A class function (or "method") is called by instance-name dot property-name.
# The instance is automatically passed as the first argument, called "self".
s.courseComplete(c1)
s.credits
s.courseComplete(c2)
s.credits

# Loop through the list of completed courses (each is a YaleCourse object)
for c in s.courses:
    print(c.department, "-", c.number)


# Even if you never create your own classes, understanding this material will
# go a long way toward helping you make sense of why Python code looks
# the way that it does.
# For example, strings in Python are actually instances of a class called "str".
# Quotation marks are a shortcut for creating strings, but you do sometimes
# explicitly use "str" to construct a string from another type of data.

z = str(3.14**2)
z

# "find", "replace", and "split" are just a few of the functions defined for
# the str class, so they can be called on "z" using the dot notation.
z.split('.')



# EXERCISE 5: Define another class called "YaleFaculty". It's __init__ function
#             should take the faculty member's name and a list of YaleCourses
#             that the faculty member teaches (an empty list by default).
#             An additional class function should be written that appends
#             a given YaleCourse to the faculty member's list
#             unless it is already on the list.






###################### ERROR HANDLING ############################

print(y)


try:
  print(y)
except:
  print("There was an error.")


try:
  print(y)
except NameError:
  print("Variable is not defined.")
except:
  print("There was an error.")



# raising Exceptions
def sqroot(x):
  if not type(x) in (int, float):
    raise TypeError("Only real numbers are allowed.")
  if x < 0:
    raise Exception("Only positive numbers are allowed.")
  return x**.5


sqroot("hi")
sqroot("1")
sqroot(-1)
sqroot(9)

# sometimes you don't really care what the error is, you just want to do
# some other default behavior without crashing the program

try:
  y = sqroot(x)
except:
  print("Error in sqroot(x), setting y to 0.")
  y = 0

y



############################## SOLUTIONS #####################################

## SOLUTION 1 ##

(1**2 + 4**2)**.5



## SOLUTION 2 ##

d = {"name": "Jill", "height": 68, "weight": 165}
people.append(d)
people



## SOLUTION 3 ##

[s.lower() for s in greeting.split() if len(s) >= 4]



## SOLUTION 4 ##

def hypotenuse(a, b):
    return (a**2 + b**2)**.5

hypotenuse(3, 4)



## SOLUTION 5 ##

class YaleFaculty:

    def __init__(self, name, courses=[]):
        self.name = name
        self.courses = courses

    def addCourse(self, course):
        if course not in self.courses:
            self.courses.append(course)
