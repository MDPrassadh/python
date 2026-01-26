int               = 10
float             = 3.14
bool              = True or False
str               = "Hello, World!"
complex           = 2 + 3j
list              = [1, 2, 3]
tuple             = (1, 2, 3)
dict              = {"key": "value"}
set               = {1, 2, 3}
frozenset         = frozenset({1, 2, 3})    
bytes             = b"Hello"
None              = None
 --- IGNORE ---

Data Types in Python:
1. int: Represents integer values.    
2. float: Represents floating-point numbers (decimal values).    
3. bool: Represents boolean values (True or False).   
4. str: Represents string values (text).
5. complex: Represents complex numbers with real and imaginary parts.    
6. list: Represents ordered, mutable collections of items.
7. tuple: Represents ordered, immutable collections of items.    
8. dict: Represents key-value pairs (dictionaries).   
9. set: Represents unordered collections of unique items.
10. frozenset: Represents immutable sets (unordered collections of unique items).    
11. bytes: Represents sequences of bytes (binary data).   
12. None: Represents the absence of a value (null value).

You can use the type() function to check the data type of a variable.

Which method is used to find the data type of a variable in Python?
You can use the type() function to find the data type of a variable in Python. For example:

x = 10
print(type(x))  # Output: <class 'int'>

x = -10
print(type(x))  # Output: <class 'int'>

x = 3.14
print(type(x))  # Output: <class 'float'>

x = True
print(type(x))  # Output: <class 'bool'>

print(True==1)
print(False==0)
output:
True
True
x = "Hello, World!"
print(type(x))  # Output: <class 'str'>

x = 2 + 3j
print(type(x))  # Output: <class 'complex'>

x = [1, 2, 3]
print(type(x))  # Output: <class 'list'>

x = (1, 2, 3)
print(type(x))  # Output: <class 'tuple'>

x = {"key": "value"}
print(type(x))  # Output: <class 'dict'>

x = {1, 2, 3}
print(type(x))  # Output: <class 'set'>

x = frozenset({1, 2, 3})
print(type(x))  # Output: <class 'frozenset'>

x = b"Hello"
print(type(x))  # Output: <class 'bytes'>

x = None
print(type(x))  # Output: <class 'NoneType'>

Note: Python is a dynamically typed language, so you don't need to explicitly declare the data type of a variable. The interpreter infers the data type based on the assigned value.  

p = 2+3j
print(type(p))  # Output: <class 'complex'>
Data Conversion in Python :
You can convert between different data types using built-in functions like int(), float(), str(), etc.

q = 5.67
print(type(q))  # Output: <class 'float'>

a = 4
print(float(a))
# output:4.0

a = 5.89
print(int(a))
# output:5


