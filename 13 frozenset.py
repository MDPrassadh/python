f=frozenset()
print(type(f))

--outpu--<class 'frozenset'>

L=[5,8,15,25]
a=frozenset(L)
print(a)

--output--frozenset({8, 25, 5, 15}) immutable

f=frozenset([8,2,6,9])
print(f)

--output--frozenset({8, 9, 2, 6})

now look at this---example for :-----

f=frozenset(5)
print(f)

--putput--:     
f=frozenset(5)
TypeError: 'int' object is not iterable

f=frozenset([15,24,45])
print((f))

--output--frozenset({24, 45, 15})

