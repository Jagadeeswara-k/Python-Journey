# Python Numbers
# int, float, complex

a=1
b=2.56
c=5j

print(a)    # int
print(b)    # float
print(c)    # complex

# -------------------------------------------------------------------------------------------------------
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x=1
y=9705233003
z=-10

print(type(x))
print(type(y))
print(type(z))

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x=10.26
y=2625.2055
z=-2.56

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.

x=5e3
y=10.E2
z=-87.5e5
print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y=5j
z=-5j

print(type(x))
print(type(y))
print(type(z))

# -------------------------------------------------------------------------------------------------------

# Type Conversion

a=10
b=2.56
c=1j

x=float(a)
y=int(b)
z=complex(x)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))