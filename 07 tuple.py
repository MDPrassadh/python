--creation and access explanation--
t = (10, 20, 30, 40, 50)
print(len(t))  # Output: 5

print(type(t))  # Output: <class 'tuple'>
print(t[0])    # Output: 10
print(t[1])    # Output: 20 
print(t[2])    # Output: 30
print(t[3])    # Output: 40
print(t[4])    # Output: 50
t[0] = 100  # This will raise a TypeError since tuples are immutable  

--slicing explanation--
a = (10, 20, 30, 40, 50, 60)
print(a[0:4:2])  # Output: (10, 30)
print(a[::3])    # Output: (10, 40) 
print(a[::-1])   # Output: (60, 50, 40, 30, 20, 10)
print(a[-1])     # Output: 60
print(a[-3])     # Output: 40
print(a[-6:-2])  # Output: (10, 20, 30, 40)
print(a[-4:-1])  # Output: (30, 40, 50)
print(a[-1:-5:-1])  # Output: (60, 50, 40, 30)
print(a[-2::-1])    # Output: (50, 40, 30, 20, 10)
print(a[-3:])       # Output: (40, 50, 60)
print(a[:-4])      # Output: (10, 20)
print(a[:])        # Output: (10, 20, 30, 40, 50, 60)
print(a[::-2])     # Output: (60, 40, 20)
print(a[-1:-7:-2]) # Output: (60, 40, 20)
print(a[5:1:-2])  # Output: (60, 40)
print(a[4:0:-2])  # Output: (50, 30)
print(a[3::-2])   # Output: (40, 20)
print(a[2:5:3])   # Output: (30,)

a=(5,8,3,2,15,6)
print(min(a))   
print(max(a))
print(sum(a))   
print(len(a))

2
15
39
6 


--concatenation explanation--

t1 = (10, 20, 30)
t2 = (40, 50, 60)
t3 = t1 + t2
print(t3)  # Output: (10, 20, 30, 40, 50, 60)   
print(t1+t2)  # Output: (10, 20, 30, 40, 50, 60)

--repetition explanation--
t4 = (10, 20, 30)
t5 = t4 * 3
print(t5)  # Output: (10, 20, 30, 10 , 20, 30, 10, 20, 30)
print(t4 * 2)  # Output: (10, 20, 30, 10, 20, 30)
print(t4 * 0)  # Output: ()

 --membership explanation--
t6 = (10, 20, 30, 40, 50)   
print(20 in t6)   # Output: True
print(60 in t6)   # Output: False
print(30 not in t6)  # Output: False
print(70 not in t6)  # Output: True 

--iteration explanation--
t7 = (10, 20, 30, 40, 50)
for item in t7:
    print(item)
10
20
30
40  
50  
 iteration over each element in the tuple and prints them one by one.   


 idnetity explanation--
 
t8 = (10, 20, 30)
t9 = t8
print(t8 is t9)  # Output: True
print(t8 is not t9)  # Output: False

# The 'is' operator checks if both t8 and t9 refer to the same object in memory, which they do since t9 is assigned to t8.  
t10 = (40, 50, 60)
print(t8 is t10)  # Output: False
print(t8 is not t10)  # Output: True
 Here, t8 and t10 are different objects in memory, so 'is' returns


False and 'is not' returns True.