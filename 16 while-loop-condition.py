while True:
    print("Python Learning")

x = 1
while True:   # infinite loop
    print(x)
    x += 1
    if x > 5:
        break   # stop the loop
    output 
1
2
3
4
5  # stop the loop

x=1        
while x<10:
    print("Hi prassadh",x)
    x+=1
output---
 
Hi prassadh 1
Hi prassadh 2
Hi prassadh 3
Hi prassadh 4
Hi prassadh 5
Hi prassadh 6
Hi prassadh 7
Hi prassadh 8
Hi prassadh 9

x = 1        
while x < 10:
    print("Hi prassadh",x)
    if x == 5:   # condition to stop
        break    # exit the loop immediately
    x += 1       # increment x
    
output----
PS D:\PYTHON-PRACTICE> & C:/Users/Admin/AppData/Local/Python/pythoncore-3.14-64/python.exe "d:/PYTHON-PRACTICE/16 while-loop-condition.py"
Hi prassadh 1
Hi prassadh 2
Hi prassadh 3
Hi prassadh 4
Hi prassadh 5
PS D:\PYTHON-PRACTICE>

count = 1
while count <= 5:
    print("Number:", count)
    count += 1   # increase count each time

output----
& C:/Users/Admin/AppData/Local/Python/pythoncore-3.14-64/python.exe "d:/PYTHON-PRACTICE/16 while-loop-condition.py"
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
PS D:\PYTHON-PRACTICE> 

count = 1
while count < 5:
    print("Number:", count)
    count += 1   # increase count each time

output----
    
& C:/Users/Admin/AppData/Local/Python/pythoncore-3.14-64/python.exe "d:/PYTHON-PRACTICE/16 while-loop-condition.py"
Number: 1
Number: 2
Number: 3
Number: 4
PS D:\PYTHON-PRACTICE> 
# 

x = 1
while True:   # infinite loop
    print(x)
    x += 1
    if x > 5:
        break   # stop the loop

output----

& C:/Users/Admin/AppData/Local/Python/pythoncore-3.14-64/python.exe "d:/PYTHON-PRACTICE/16 while-loop-condition.py"
1
2
3
4
5
PS D:\PYTHON-PRACTICE> 


num = 0
while num < 5:
    num += 1
    if num == 3:
        continue   # skip printing 3
    print(num)

Alright Durga, let’s dissect this **line by line** and really understand what’s happening under the hood.  

---

### 🔍 Code
```python
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue   # skip printing 3
    print(num)
    
```

---

## Step-by-Step Execution

1. **Initialization**  
   - `num = 0`

2. **First loop iteration**  
   - Condition: `num < 5` → `0 < 5` ✅ True  
   - `num += 1` → `num = 1`  
   - `if num == 3` → `1 == 3` ❌ False  
   - `print(num)` → prints `1`

3. **Second iteration**  
   - Condition: `1 < 5` ✅ True  
   - `num += 1` → `num = 2`  
   - `if num == 3` → `2 == 3` ❌ False  
   - `print(num)` → prints `2`

4. **Third iteration**  
   - Condition: `2 < 5` ✅ True  
   - `num += 1` → `num = 3`  
   - `if num == 3` → `3 == 3` ✅ True  
   - `continue` → skips the `print(num)` line and jumps back to the top of the loop.  
   - **Nothing printed here.**

5. **Fourth iteration**  
   - Condition: `3 < 5` ✅ True  
   - `num += 1` → `num = 4`  
   - `if num == 3` → `4 == 3` ❌ False  
   - `print(num)` → prints `4`

6. **Fifth iteration**  
   - Condition: `4 < 5` ✅ True  
   - `num += 1` → `num = 5`  
   - `if num == 3` → `5 == 3` ❌ False  
   - `print(num)` → prints `5`

7. **Sixth iteration**  
   - Condition: `5 < 5` ❌ False  
   - Loop ends.

---

## 🧑‍💻 Final Output
```
1
2
4
5
```

---

## ⚙️ Deep Analysis of Key Concepts

- **`while num < 5`** → loop runs until `num` reaches 5.  
- **`num += 1`** → increments `num` each time, preventing infinite loop.  
- **`if num == 3: continue`** → when `num` is 3, the loop **skips the rest of the block** and goes back to the condition check. That’s why `3` is missing in the output.  
- **Control flow**:  
  - `break` → stops the loop entirely.  
  - `continue` → skips just the current iteration, but keeps looping.  

---

👉 In short: this loop prints numbers 1 to 5, but **skips 3** because of the `continue`.  

Would you like me to also show you a **trace table** (row-by-row table of `num` values and actions) so you can visualize the loop flow even more clearly? 



a=5
while a<15:
    print("python learning",a)
    
    a+=1

--output----

PS D:\PYTHON-PRACTICE> & C:/Users/Admin/AppData/Local/Python/pythoncore-3.14-64/python.exe "d:/PYTHON-PRACTICE/16 while-loop-condition.py"
python learning 5
python learning 6
python learning 7
python learning 8
python learning 9
python learning 10
python learning 11
python learning 12
python learning 13
python learning 14
PS D:\PYTHON-PRACTICE> 
    
