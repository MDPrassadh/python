# a=[]
# print(type(a))  # <class 'list'>
# a=[1,2,3,4,5]
# print(a)  # [1, 2, 3, 4, 5]
# print(type(a))  # <class 'list'>

# a=["mahesh",10,20.5,True]
# print(a)  # ['mahesh', 10, 20.5, True]  
# print(a[0]) 
# print(a[3]) # mahesh
# print(type(a))  # <class 'list'>    
# a=[1,2,3,4,5]
# print(a[0])  # 1    

# print(a[1])  # 2
# print(a[2])  # 3    
# print(a[3])  # 4
# print(a[4])  # 5
# print(a[-1])  # 5
# print(a[-2])  # 4   
# print(a[-3])  # 3
# print(a[-4])  # 2
# print(a[-5])  # 1

# slice in list explanation----------
#start -stop-skip

# a=["mahesh babu",10,20.5,True,"ntr","ram charan"]

# print(a[0]) # mahesh babu
# print(a[0:5:1]) # ['mahesh babu', 10, 20.5, True, 'ntr']
# print(a[0:5:2]) # ['mahesh babu', 20.5, 'ntr']
# print(a[0:5:3]) # ['mahesh babu', True]

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print(numbers[1:4])     # [20, 30, 40] → from index 1 to 3
# print(numbers[:3])      # [10, 20, 30] → from start to index 2
# print(numbers[2:])      # [30, 40, 50] → from index 2 to end
# print(numbers[::2])     # [10, 30, 50] → every 2nd element
# print(numbers[::-1])    # [50, 40, 30, 20, 10] → reversed list

# print(numbers[0:10:3])  # [10, 40, 70, 100]


# a= [10, 20, 30, 40, 50, 60]

# print(a[1:5:2])  # [20, 40]

# Methods in list:
# # append
# # extend
# insert    
# remove
# pop
# clear
# index 
# count
# sort
# reverse
# copy  
# append and extend-examples
# a=[10,20,30,"MB",True,"PSPK",40.5,"REBEL"]
# a.append("NTR")
# print(a) 
# a.extend(["NTR","RAMCHARAN"])
# print(a)

# count-examples
# a=[10,20,30,10,40,10,50,10]
# print(a.count(10))  # 4 
# print(a.count(50)) # 1
# print(a.count(100)) # 0
# print(a.count(20)) # 1
# print(a.count(30)) # 1


# # remove-examples
# a=[10,20,30,10,40,10,50,10] 
# a.remove(10)
# print(a)  # [20, 30, 10, 40, 10, 50, 10]
# # i want to remove all 10s from the list
# a=[10,20,30,10,40,10,50,10] 
# while 10 in a:
#     a.remove(10)
# print(a)  # [20, 30, 40, 50]    


# a = [10, 20, 30, 10, 40, 10, 50, 10]
# a = [x for x in a if x != 10]
# print(a)   # [20, 30, 40, 50]



# a = [10, 20, 30, 10, 40, 10, 50, 10]
# a = [x for x in a if x == 10]
# print(a)  # [10, 10, 10, 10]


# pop-examples
# a=[10,20,30,40,50,20,30]

# a.pop()  # removes last element
# print(a)  # [10, 20, 30, 40, 50, 20]

# a.pop(2)  # removes element at index 2  
# print(a)  # [10, 20, 40, 50, 20]

# a.pop(0)  # removes element at index 0  
# print(a)  # [20, 40, 50, 20]  
  
# a.pop(1)  # removes element at index 1  
# print(a)  # [20, 50, 20]

# a.pop(5)  # IndexError: pop index out of range  
# print(a)  # [20, 50, 20]

# a.pop(-1)  # removes last element  
# print(a)  # [20, 50]

# # Index -examples
# a=[10,20,30,40,50,20,30,"MD","PSPK"]
# print(a.index(10))  # 0
# print(a.index(20))  # 1 
# print(a.index(30))  # 2
# print(a.index(40))  # 3 
# print(a.index("PSPK"))  # 8

# Insert-examples
# a=[10,20,30,40,50,"PK","MD"]
# a.insert(2,"MB")
# print(a)  # [10, 20, 'MB', 30, 40, 50, 'PK', 'MD']
# print(len(a))  # 8

