a={ }
print(type(a))

d={2:'xy', 25:'mahesh',5:'arjun'}
print(d)

print(d[25])   #---output--mahesh
print(d[5])    #---output--arjun
print(d[2])    #---output--xy

____ get-examples

d={2:'xy', 25:'mahesh',5:'arjun'}
print(d)
print(d.get(5)) 
# output arjun
print(d.keys())
# output --dict_keys([2, 25, 5])

---values-examples

print(d.values())
# output --dict_values(['xy', 'mahesh', 'arjun'])
d={2:'xy', 25:'mahesh',5:'arjun'}
print(d)

print(d.values())

print(d.get(2))
print(d.values(xy)) # not possible in this way
d={2:'xy', 25:'mahesh',5:'arjun'}
print(d)

--items-examples

print(d.items())

{2: 'xy', 25: 'mahesh', 5: 'arjun'}
dict_items([(2, 'xy'), (25, 'mahesh'), (5, 'arjun')])

update --examples
d={2:'xy', 25:'mahesh',5:'arjun'}
print(d)
print(d.update({6:100}))
print(d)

print(d.values())
print(d.items())

{2: 'xy', 25: 'mahesh', 5: 'arjun'}
None
{2: 'xy', 25: 'mahesh', 5: 'arjun', 6: 100}
dict_values(['xy', 'mahesh', 'arjun', 100])
dict_items([(2, 'xy'), (25, 'mahesh'), (5, 'arjun'), (6, 100)]