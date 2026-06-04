# The print() function is used to display output on the screen.
"""
1. Output Function → print()
2. Single Quote → 'Python'
3. Double Quote → "Python"
4. Triple Quote → Multi-line text
5. New Line → \n
6. Separator → sep
7. Line Ending → end
"""
#--------------------------------------------------------------------------------------
# Double Quotes
print("Welcome to python learning")

# Single Quotes
print('Welcome to vs code to learn python')

# Differene
print("I'am learning a python")
# print('I'am learning python') - It gives error
print('I\'am learnig python')  # It i will not give u error

#--------------------------------------------------------------------------------------

# Triple Double quotes
print("""
      python
      java
      c
      cpp
      """)

# Triple Single quotes
print('''
      python
      java
      c
      cpp
      ''')

#--------------------------------------------------------------------------------------

# Multi line Printing 
# Method -1

print("Python")
print("Java")
print("C and Cpp")

# Method - 2

print("Python \njava \nC and Cpp ")

#--------------------------------------------------------------------------------------
# Seperator
print("python", "Java", "C and CPP","A=B")
print("python", "Java", "C and CPP","A=B", sep=" | ")
print(10 ,20, 30, 40, 50, sep=" | ")

#--------------------------------------------------------------------------------------
# using End Parameter

print("Python", end=" ")
print("Java")

#--------------------------------------------------------------------------------------
# Printing Numbers
print(100)      # number
print(99.99)    # float
print(True)     # boolean
print(False)    # boolean

#--------------------------------------------------------------------------------------
# Printitng variables
name="Alex"
print(name)