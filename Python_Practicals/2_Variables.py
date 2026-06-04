# Variables are containers for storing data values.

x=5             # int
a=10.26         # float
y="Jagadeesh"   # Character

print(x)
print(y)

#------------------------------------------------------------------------------------------------------------

# Casting - If you want to specify the data type of a variable, this can be done with casting.

x=50
y=50.2

print(float(x)) # 50.0
print(str(x))   # 50
print(int(y))   # 50

#------------------------------------------------------------------------------------------------------------

# Get the Type - You can get the data type of a variable with the type() function.

x=6
y="Jagadeesh"
z=5.026

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

#------------------------------------------------------------------------------------------------------------

# Case-Sensitive - Variable names are case-sensitive.

A=10
a="jagadeesh"

print(a)
print(A)

#------------------------------------------------------------------------------------------------------------

"""
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#------------------------------------------------------------------------------------------------------------
# Camel Case - Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Snake Case - Each word is separated by an underscore character:
my_variable_name = "John"

# Pascal Case - Each word starts with a capital letter:
MyVariableName = "John"

#------------------------------------------------------------------------------------------------------------

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x,y,z = "orange", "Bannana", "Cherry"

print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"

print(x)
print(y)
print(z)

# Unpack a Collection
# you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "bananna", "carrot"]
x, y,z = fruits

print(x)
print(y)
print(z)

#------------------------------------------------------------------------------------------------------------

# Output Variables
x="python is programming"
print(x)

x="Python"
y="is"
z="Programming"
print(x, y, z)

x="Python "
y="is "
z="Programming"
print(x + y + z)


x=5
y=10
print(x+y)

x=20
y="Jagadeesh"
print(x, y)

#------------------------------------------------------------------------------------------------------------

# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

x = "jagadeesh"

def myfun():
    print("Python is " + x)

myfun()

x ="Jagadeesh"

def myfun():
    x="Mohan"
    print("Python is " + x)

myfun()
print("Python is " + x)

#----------------------------------------------------
def myfun():
    global x
    x="Fanstatic"

myfun()
print("Python is " + x)


x="apple"

def myfun():
    global x
    x="Bananna"
myfun()

print("Fruit is " + x)

