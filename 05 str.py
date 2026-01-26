# string is collection of characters
'''
single quotes
double quotes
triple quotes
# '''
a='hello'
b="hello"
c='''hello'''
print(type(a)),type(b),type(c))
print(type(a))
print(type(b))
print(type(c))  


print(a)
print(b)    
print(c)
print(type(a)),type(b),type(c))

print(type(a))
print(type(b))    
print(type(c))

STRING METHODS:
1. len(): Returns the length of the string.
2. lower(): Converts all characters in the string to lowercase.   
3. upper(): Converts all characters in the string to uppercase.
4. strip(): Removes leading and trailing whitespace from the string.  
5. lstrip(): Removes leading whitespace from the string.
6. rstrip(): Removes trailing whitespace from the string. 
7. replace(): Replaces occurrences of a specified substring with another substring.
8. split(): Splits the string into a list of substrings based on a specified delimiter.
9. join(): Joins a list of strings into a single string using a specified delimiter.
10. find(): Returns the lowest index of the substring if found in the string.  
11. format(): Formats the string using placeholders.
12. isalpha(): Returns True if all characters in the string are alphabetic.   
11. isdigit(): Returns True if all characters in the string are digits.
12. isspace(): Returns True if all characters in the string are whitespace.   
13 endswith(): Returns True if the string ends with the specified suffix.
14. startswith(): Returns True if the string starts with the specified prefix.    
15 remove prefix() : removes the specified prefix from the string if it exists.
16 remove suffix() : removes the specified suffix from the string if it exists.   
17 count(): Returns the number of occurrences of a substring in the string.   
18 index(): Returns the lowest index of the substring if found in the string.  
19 capitalize(): Capitalizes the first character of the string.
20 count(): Returns the number of occurrences of a substring in the string.
21 title(): Converts the first character of each word to uppercase.
22 swapcase(): Swaps the case of each character in the string.    
23 zfill(): Pads the string with leading zeros to a specified width.
24 center(): Centers the string within a specified width, padding with spaces.    


EXPLANATIONS AND EXAMPLES OF STRING METHODS:
1. len(): Returns the length of the string.
print(example:  len("hello") returns 5)   

# lower(): Converts all characters in the string to lowercase.   
print(example:  "HELLO".lower() returns "hello"
a= "MAHESH BABU"
print(a.lower())

a= "kalyanbabu"
print(a.upper())

ENDSWITH ---BOOLEAN VALUE
a="Mahesh Babu"
print(a.endswith("Babu"))  # TRUE
print(a.endswith("babu"))  # FALSE
print(a.endswith("u"))     # TRUE
print(a.endswith("Mahesh")) # FALSE
print(a.startswith("Mahesh")) # TRUE
print(a.startswith("mahesh")) # FALSE
print(a.startswith("M"))      # TRUE    
print(a.startswith("Babu"))   # FALSE

REPLACE EXAMPLES:--------
a="Mahesh babu"
print(a.replace("babu","Kumar"))  # Mahesh Kumar
print(a.replace("Mahesh","Raj"))   # Raj babu

Index EXAMPLES:--------

a="Mahesh babu"
# print(a.index("babu"))  # 7
# print(a.index("M"))     # 0
# print(a.index("h"))     # 3   
print(a.index("Mahesh"))     # 0
# print(a.index("z"))     # ValueError: substring not found 

# FIND EXAMPLES:--------
a="Prabash Raju"
print(a.find("NTR")) # -1
print(a.find("Raju"))   # 0
print(a.find("Prabash"))      # 0

COUNT EXAMPLES:--------
a="Mahesh babu"

print(a.count("babu"))   # 1    
print(a.count("z"))      # 0
print(a.count("Mahesh")) # 1
print(a.count("u"))     # 1
print(a.count("a")) # 2
print(a.count("h")) # 2
print(a.count("e")) # 1 
print(a.count("b")) # 2

# prefix EXAMPLES:--------
a="unhappiness is a state of mind"
print(a.removeprefix("un"))   # happiness is a state of mind
print(a.removeprefix("unhappiness"))  # unhappiness is a state of mind    
print(a.removeprefix("is"))  # unhappiness is a state of mind
print(a.removeprefix("state"))  # unhappiness is a state of mind

suffix EXAMPLES:--------
a="happiness is a state of mindless"
print(a.removesuffix("less"))   # happiness is a state of mind
print(a.removesuffix("mindless"))  # happiness is a state of       

split EXAMPLES:--------
a="Durga Prasad M"
print(a.split())  # ['Durga', 'Prasad', 'M']
['Durga', 'Prasad', 'M']

# strip EXAMPLES:--------
a="   Mahesh Babu   "
print(a.strip())  # "Mahesh Babu".

# lstrip EXAMPLES:--------
a="   Mahesh Babu   "     
print(a.lstrip())  # "Mahesh Babu   ".

# rstrip EXAMPLES:--------
a="   Mahesh Babu   "     
print(a.rstrip())  # "   Mahesh Babu".

 