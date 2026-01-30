 NESTED-FOR-LOOP

for i in range (0,5):
    for j in range (0,3):
        print(i,j)
        
--output---
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
3 0
3 1
3 2
4 0
4 1
4 2

for i in range (0,5):
    for j in range (0,3):
        print(i+j)
# --output--
0
1
2
2
3
2
3
4
3
4
5
4
5
6

for i in range(3):        # Outer loop
    for j in range(2):    # Inner loop
        print(f"i={i}, j={j}")
#--output---
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1

***  Multiplication Table

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()

#--output--
1 2 3 4 5 
2 4 6 8 10    
3 6 9 12 15   
4 8 12 16 20  
5 10 15 20 25 

##--Working with 2D Lists (Matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for row in matrix:          # Outer loop → goes through each sublist
    for value in row:       # Inner loop → goes through each element in that sublist
        print(value, end=" ")
    print()                 # Moves to the next line after finishing a row

matrix is a list of lists (3 rows, each with 3 values).

The outer loop picks one row at a time: [1,2,3], then [4,5,6], then [7,8,9].

The inner loop iterates through each element of that row.

end=" " ensures values print on the same line separated by spaces.

print() after the inner loop moves to the next line.

#--output--
1 2 3 
4 5 6 
7 8 9 



flat = [value for row in matrix for value in row]
print(flat)

#--output--

[1, 2, 3, 4, 5, 6, 7, 8, 9]