Looping Statements:----

for i in range   [-----this is the syntax for loop]
    print(i)

i want loop of (0,10) print so here is syntax for that

for i in range(10):  #(0,10)
    print(i)
    
#--output--
0
1
2
3
4
5
6
7
8
9

Now i need a slice of upto 10 numbers slicing like this
for i in range(0,10,2):
    print(i)
    
#output--
0
2
4
6
8

Now i need a slice of upto 10 numbers slicing like this
for i in range(1,10,2):
    print(i)
    
#output--
1
3
5
7
9

r=[2,4,6,7,9]  # here im using list
for i in r:
    print(i)

#output--
2
4
6
7
9

L=[8,3,5,15]
for i in L:
    print(i)
    
# output--
8
3 
5 
15
    

---Nested for loop------------

for i in (0,5):
    for j in (0,3):
        print(i,j)
        
output---------
& C:/Users/Admin/AppData/Local/Python/pythoncore-3.14-64/python.exe "d:/PYTHON-PRACTICE/16 while-loop-condition.py"
0 0
0 3
5 0
5 3

for loop with list------
a=[8,4,59,23]  # list we can take here unorder result also
for i in a:
     print(i)
     
--output------
PS D:\PYTHON-PRACTICE> & C:/Users/Admin/AppData/Local/Python/pythoncore-3.14-64/python.exe "d:/PYTHON-PRACTICE/16 while-loop-condition.py"
8
4
59
23
PS D:\PYTHON-PRACTICE> 

for loop with string------

a="prassadh"
for i in a:
    print(i)

--output---------
& C:/Users/Admin/AppData/Local/Python/pythoncore-3.14-64/python.exe "d:/PYTHON-PRACTICE/16 while-loop-condition.py"
p
r
a
s
s
a
d
h
PS D:\PYTHON-PRACTICE> 
