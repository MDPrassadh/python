'''**File handling in Python is the process of creating, opening, reading, writing, and closing files, allowing you to store and retrieve data permanently. It is different from exception handling, but the two often work together because file operations can fail (e.g., missing file, permission errors).**  

---

## 📂 What is File Handling?
- **Definition**: Managing files on disk through Python code.
- **Purpose**: Store data permanently, process external files (like `.txt`, `.csv`, `.json`), and automate tasks such as logging or configuration management.
- **Key Benefit**: Unlike variables (which vanish when the program ends), files preserve data across sessions.

---

## 🔑 Core Operations

### 1. Opening Files
- Use the built-in `open()` function:
  ```python
  file = open("example.txt", "r")
  ```
- **Modes**:
  - `"r"` → read (default)
  - `"w"` → write (creates/overwrites file)
  - `"a"` → append (adds to end of file)
  - `"x"` → create new file (error if exists)
  - `"b"` → binary mode (e.g., images)
  - `"t"` → text mode (default)

### 2. Reading Files
- `file.read()` → reads entire file.
- `file.readline()` → reads one line.
- `file.readlines()` → returns list of all lines.

Example:
```python
with open("example.txt", "r") as f:
    data = f.read()
    print(data)
```

### 3. Writing Files
- `file.write("Hello")` → writes text.
- `file.writelines(["line1\n", "line2\n"])` → writes multiple lines.

Example:
```python
with open("example.txt", "w") as f:
    f.write("Hello, Durga!\n")
```

### 4. Closing Files
- Always close after use:
  ```python
  file.close()
  ```
- Or use `with` (context manager) which auto-closes.

---

## ⚠️ Exception Handling with Files
File handling often requires **exception handling**:
```python
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
```
- Prevents crashes if file doesn’t exist.
- Common exceptions: `FileNotFoundError`, `PermissionError`, `IOError`.

---

## 📊 Summary Table

| Concept              | Purpose                          | Example Code |
|----------------------|----------------------------------|--------------|
| Open a file          | Access file for read/write       | `open("f.txt","r")` |
| Read a file          | Get data from file               | `f.read()` |
| Write a file         | Save data to file                | `f.write("Hi")` |
| Append to file       | Add data without overwriting     | `open("f.txt","a")` |
| Close a file         | Release system resources         | `f.close()` |
| Exception handling   | Handle errors safely             | `try...except` |

---

## 🚀 Advanced File Handling
- **Binary files**: Handle images, audio, etc. using `"rb"` or `"wb"`.
- **File methods**: `seek()`, `tell()` for cursor movement.
- **OS module**: `os.remove()`, `os.rename()` for file management.
- **Pathlib**: Modern way to handle paths and files (`Path("file.txt").read_text()`).

---

✅ In short: **File handling = working with files (open, read, write, close). 
Exception handling = managing errors. They are different but often used 
together for safe file operations.**

Durga, since you like systematic mastery, would you like me to prepare 
a **practice set of file handling tasks** (like creating, reading, 
appending, and handling errors) so you can try them step by step?
'''

'''
File Hnadling in Python
Create
Open
Read
Write
Append
close



u=open('26 file-handling.txt','r')
print(u.read())
u.close()

# output---
# & C:/Users/Admin/AppData/Local/Python/pythoncore-3.14-64/python.exe "d:/PYTHON-PRACTICE/25 File-Handling.py"
# Hello Welcome to python world
# PS D:\PYTHON-PRACTICE> 

also read like this :------------

with open("26 file-handling.txt", "r") as f:
    data = f.read()
    print(data)


u=open('26 file-handling.txt','w')
u.write('Python With SIDDU')
u.close()

just it is writing only but nw i want ot write and again read also then 



# Write to file
with open('26 file-handling.txt', 'w') as u:
    u.write('Python With MDP')

# Read from file
with open('26 file-handling.txt', 'r') as u:
    content = u.read()
    print(content)


Shortcut (write + read without reopening)
If you want to write and then immediately read in the same block, open in read/write mode ('w+'):

with open('26 file-handling.txt', 'w+') as u:
    u.write('Python With SIDDU')
    u.seek(0)              # move cursor back to start
    print(u.read())



# with open('26 file-handling.txt', 'w+') as u:
#     u.write('MDP')
#     u.seek(0)              # move cursor back to start
#     print(u.read())
'''

u=open('26 file-handling.txt','w')
u.write('Python With SIDDU\n')
u.write('Python With MDP\n')
u.close()

'''
If you want to write and then immediately read in the same block, open in read/write mode ('w+'):
    
with open('26 file-handling.txt','w+') as u:
    u.writelines([
        'Python With SIDDU\n',
        'Python With MDP\n'
        'Heloo Bulli sir\n'
        ])
    u.seek(0)
    print(u.read())
'''

s=open('26 file-handling.txt','a')
s.write('Mamatha')
s.close()

s=open('26 file-handling.txt','a+')
s.write('BM')
s.seek(0)
print(s.read())


If you want to write multiple lines at once, you can use writelines():


with open('26 file-handling.txt','w') as u:
    u.writelines([
        'Python With SIDDU\n',
        'Python With MDP\n'
    ])