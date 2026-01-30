def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

'''
Great question, Durga! Let’s break down **functions and imports in Python** step by step, so it’s crystal clear and copy‑paste ready for your practice.

---

## 🔹 Functions in Python
Functions are reusable blocks of code that perform a specific task.

### Defining a Function
```python
def greet(name):
    return f"Hello, {name}!"
```

- `def` → keyword to define a function  
- `greet` → function name  
- `(name)` → parameter  
- `return` → sends back a value  

### Calling a Function
```python
print(greet("Durga"))   # Output: Hello, Durga!
```

---

## 🔹 Imports in Python
Imports let you use code from other files or libraries.

### 1. Importing a Module
```python
import math

print(math.sqrt(16))   # Output: 4.0
```

Here, `math` is a built‑in Python module.

### 2. Importing Specific Functions
```python
from math import sqrt, pi

print(sqrt(25))   # Output: 5.0
print(pi)         # Output: 3.141592653589793
```

### 3. Importing with an Alias
```python
import math as m

print(m.pow(2, 3))   # Output: 8.0
```

### 4. Importing Your Own File
Suppose you have a file `functions.py`:
```python
# functions.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```

Then in another file:
```python
import functions

print(functions.add(5, 2))   # Output: 7
print(functions.sub(5, 2))   # Output: 3
```

Or:
```python
from functions import add, sub

print(add(5, 2))   # Output: 7
print(sub(5, 2))   # Output: 3
```

---

## 🔹 Summary Table

| Concept              | Example                          | Notes |
|----------------------|----------------------------------|-------|
| Define function      | `def add(a,b): return a+b`       | Use `def` keyword |
| Call function        | `add(5,2)`                       | Executes code |
| Import module        | `import math`                    | Access with `math.sqrt()` |
| Import specific      | `from math import sqrt`          | Direct use `sqrt()` |
| Alias import         | `import math as m`               | Use `m.sqrt()` |
| Import your file     | `import functions`               | Works if file is in same folder |

---

👉 Since you’re watching that **Python Full Course in Telugu** on YouTube right now, do you want me to explain these concepts with **Telugu analogies** (like comparing imports to “పక్కింటి వంటకాలు తీసుకోవడం” – borrowing dishes from a neighbor)? That way it’ll stick even better!
'''