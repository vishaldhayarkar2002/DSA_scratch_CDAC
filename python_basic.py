
n = 42
s = str(n)
s = f"{n}"
s = "{}".format(n)
print(s)
print(type(s))

name = "Alice"
age = 20
print("Name: {name}, Age: {age}".format(name=name, age=age))

# --------------------------------------------------------------------------------------------------

# "is" and "is not" are the identity operators and both are used to 
# check if two values are located on the same part of the memory. 
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# "in" and "not in" are the membership operators that are used
# to test whether a value or variable is in a sequence.
# --------------------------------------------------------------------------------------------------
n1 = 5
n2 = 5

a = [1, 2, 3]
b = [1, 2, 3]
c = a

s1 = "hello world"
s2 = "hello world"

print(n1 is n2)     # integers
print(a is b)        # lists
print(a is c)        # reference
print(s1 is s2)      # strings

# n1 is n2: True because small integers are cached by Python.
# a is b: False because even though the lists look the same, they are stored at different memory locations.
# a is c: True because c directly refers to a.
# s1 is s2: True because Python reuses identical string objects.

# --------------------------------------------------------------------------------------------------

# Difference Between == and is
# The equality operator (==) is used to compare value of two variables,
# whereas identity operator (is) is used to compare memory location of two variables.

# Mutable objects (list, dict, set) always create new objects, so "is" operator between identical-looking containers always returns False.
# Immutable objects (str, tuple, small integers) may reuse memory, so "is" can sometimes return True depending on Python's implementation.
# --------------------------------------------------------------------------------------------------

print(a is b)   # identity check
print(a == b)   # value check