
for i in {2: 'xy', 25: 'mahesh', 5: 'arjun', 6: 100}:
        print(i)
2
25
5 
6   
 # here dictionary ending {2: 'xy', 25: 'mahesh', 5: 'arjun', 6: 100}: 
 # so only display keys not like that 
#  for i in {2:'xy',25:'mahesh',5:'arjun',6:100}.values():
#          print(i)

for i in {2: 'xy', 25: 'mahesh', 5: 'arjun', 6: 100}.values():
        print(i)
# output 
# xy    
#mahesh
#arjun 
#100  

for i in {2: 'xy', 25: 'mahesh', 5: 'arjun', 6: 100}.items():
        print(i)
output
(2, 'xy')     
(25, 'mahesh')
(5, 'arjun')
(6, 100)

for i in {2: 'xy', 25: 'mahesh', 5: 'arjun', 6: 100}.keys():
        print(i)
        
        # output---
# 2
# 25
# 5 
# 6 
for i in {2: 'xy', 25: 'mahesh', 5: 'arjun', 6: 100}:
        print(i)
        
output---
2 
25
5 
6 

Here Both output are smae when you mentions .keys(): or : only result the same 

for i,j in {2: 'xy', 25: 'mahesh', 5: 'arjun', 6: 100}.items():
        print(i,j)
        
output---like this means
2 xy
25 mahesh
5 arjun  
6 100  

for i,j in {2: 'xy', 25: 'mahesh', 5: 'arjun', 6: 100}.items():
        print(i,j)




