"""
Python has the following data types built-in by default, in these categories:

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
"""
a = "jaagdeesh"     # sting
b = 10              # int
c = 50.20           # float
d = 5j+2j           # complex

e = ["apple", "Bananna", "Mango"]   # list
f = ("apple", "bananna", "Mango")   # Tuple

g = range(6)
h = {"Name" : "Jagadeesh", "age" : 26}  # Dict
i = {"Apple", "Bananna", "mango"}       # set
j = frozenset({"Appple", "Bananna", "Mango"})   # Frozenset
k= True     # bool
l = b"Hello"    # byte
m = bytearray(5)
n= memoryview(bytes(5))   #memeory view
o =None     # none Type

print(m)
print(n)