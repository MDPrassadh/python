Mostly set{} operations are 
1 Union 
2 intersection
3 difference
4 is subset
5 is superset

1 Union-SET Examples 
A={4,5,6}
B={7,5,9}
print(A.union(B))

-outpu---{4, 5, 6, 7, 9}  dupication not repeat

2 intersection
A={4,5,6}
B={7,5,9}
print(A.intersection(B))

#-outpu---{5}

3 Difference
A={4,5,6}
B={7,5,9}
print(A.difference(B))

-outpu---{4, 6}

4 is subset & Superset

A={1,2,3,4,5,6,}
B={3,4,6}
print(B.issubset(A))
# True
print(A.issubset(B))
# False
print(A.issuperset(B))
# True
print(B.issuperset(A))
# False
