'''
function definition -- it has paraemters

function call --it has aruguments
'''

'''
def functionname():     # function definition
    print("This is first function in python")
    
functionname()    # function call
'''

'''
# ---output-------
# PS D:\PYTHON-PRACTICE> & C:/Users/Admin/AppData/Local/Python/pythoncore-3.14-64/python.exe "d:/PYTHON-PRACTICE/19 function.py"
# This is first function in python 
'''

'''
def functionname():     # function definition
    print("This is first function in python")
    
functionname()    # function call
functionname()
functionname()
functionname()
'''

'''
This is first function in python
This is first function in python
This is first function in python
This is first function in python How many time you call the function it will call and return also code reusable...
'''

'''
def receipe():
    print("chicken")
    print("curd")
    print("coriander")
    print("ginger")
    print("etc")
receipe()
receipe()
receipe()
receipe()
'''


'''
chicken  
curd     
coriander
ginger   
etc  
'''

'''
def add(a,b):
    return(a+b)
print(add(5,2))

# output---7 
'''

'''
def prassadh(a,b,c):
    print("This is prassadh first function",a,b,c)
    
prassadh(2,3,4)

#--output--This is prassadh first function 2 3 4
'''

'''
def prassadh(*a):
    print("This is prassadh first function",a)
    
prassadh(2,3,4)


--output--This is prassadh first function 2 3 4
'''
'''
def prassadh(**a):
    print("This is Touple formats comes from ** given",a)

prassadh(a=2,b=6)

---output--This is Touple formats comes from ** given {'a': 2, 'b': 6}
'''


'''
--------NESTED FUNCTION-----------------

def outer():
        print("outer function print")
     
        def inner():
         print("inner fucntion print")
        inner()
outer()
        
# output---
# outer function print
# inner fucntion print
'''
       



'''
# You can pass any number of arguments (including none).

# python
# prassadh()          # Output: This is prassadh first function ()
# prassadh(1)         # Output: This is prassadh first function (1,)
# prassadh(1,2,3,4,5) # Output: This is prassadh first function (1, 2, 3, 4, 5)
# The arguments are stored in a tuple, so you can loop over them:

# python
# def prassadh(*a):
#     for value in a:
#         print("Got:", value)

# prassadh(10, 20, 30)
# Output:

# Code
# Got: 10
# Got: 20
# Got: 30
'''







'''
First Function: Fixed Parameters
python
def prassadh(a, b, c):
    print("This is prassadh first function", a, b, c)

prassadh(2, 3, 4)
How it works:
The function explicitly defines three parameters: a, b, c.

When you call prassadh(2,3,4), Python matches:

a = 2

b = 3

c = 4

Inside the function, it prints them individually.

Output:
Code
This is prassadh first function 2 3 4
Key points:
You must pass exactly 3 arguments.

If you pass fewer or more, Python raises an error:

python
prassadh(2,3)   # TypeError: missing 1 required positional argument
prassadh(2,3,4,5) # TypeError: takes 3 positional arguments but 4 were given
🔹 Second Function: Variable-Length Arguments (*args)
python
def prassadh(*a):
    print("This is prassadh first function", a)

prassadh(2, 3, 4)
How it works:
The *a syntax means: collect all positional arguments into a tuple named a.

When you call prassadh(2,3,4), Python packs them into:

a = (2, 3, 4)

Inside the function, it prints the tuple.

Output:
Code
This is prassadh first function (2, 3, 4)
Key points:
You can pass any number of arguments (including none).

python
prassadh()          # Output: This is prassadh first function ()
prassadh(1)         # Output: This is prassadh first function (1,)
prassadh(1,2,3,4,5) # Output: This is prassadh first function (1, 2, 3, 4, 5)
The arguments are stored in a tuple, so you can loop over them:

python
def prassadh(*a):
    for value in a:
        print("Got:", value)

prassadh(10, 20, 30)
Output:

Code
Got: 10
Got: 20
Got: 30
🔹 Deep Difference
Feature	def prassadh(a,b,c)	def prassadh(*a)
Parameters	Fixed (exactly 3)	Flexible (any number)
Argument passing	Must match count	Packs into a tuple
Error handling	Raises error if count mismatched	Never errors on count (unless you require at least one)
Use case	When you know the exact number of inputs	When you want flexibility (unknown number of inputs)
🔹 Analogy
Think of it like seating in a bus:

def prassadh(a,b,c) → exactly 3 seats. If you bring 2 or 4 people, it won’t work.

def prassadh(*a) → unlimited seats. Whoever comes in, they all sit, and you can check later how many came.

👉 Durga, since you’re exploring Python systematically, the next step is to look at **kwargs (double star), which collects keyword arguments into a dictionary. That’s the sibling of *args.

Would you like me to show you a combined example of *args and **kwargs together, so you see how Python handles both positional and keyword arguments flexibly?

Third Function: Keyword Arguments (**kwargs)
python
def prassadh(**kwargs):
    print("This is prassadh keyword function", kwargs)

prassadh(name="Durga", skill="Python", level="Hero")
How it works:
The **kwargs syntax collects all keyword arguments into a dictionary.

When you call prassadh(name="Durga", skill="Python", level="Hero"), Python packs them into:

python
kwargs = {"name": "Durga", "skill": "Python", "level": "Hero"}
Inside the function, you can access values by their keys.

Output:
Code
This is prassadh keyword function {'name': 'Durga', 'skill': 'Python', 'level': 'Hero'}
🔹 Combined Function: *args and **kwargs
python
def prassadh(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

prassadh(1, 2, 3, name="Durga", skill="Python", level="Hero")
How it works:
*args → collects positional arguments into a tuple: (1, 2, 3)

**kwargs → collects keyword arguments into a dictionary: {'name': 'Durga', 'skill': 'Python', 'level': 'Hero'}

Both can be used together in one function.

Output:
Code
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Durga', 'skill': 'Python', 'level': 'Hero'}
🔹 Deep Difference
Feature	*args (tuple)	**kwargs (dict)
Collects	Positional arguments	Keyword arguments
Data structure	Tuple	Dictionary
Flexibility	Any number of values	Any number of key-value pairs
Access style	By index (args[0])	By key (kwargs["name"])
Use case	Unknown count of values	Optional named parameters
🔹 Analogy
Think of it like a party:

*args → guests who just show up (no labels, just numbers).

**kwargs → guests who sign in with name tags (key-value pairs).

Combined → you can handle both groups together.

'''
