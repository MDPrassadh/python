ADD in set

a={20,25,47,69,2}
a.add(5)
print(a)
--output-- {2, 20, 69, 5, 25, 47}

nuber will add in anywhere in set but not sure of place we can use add one number at a time ..
if you need more than one number in set use "update"

UPDATE  in set
a={20,25,47,69,2}
a.update({1,7,11})
print(a)
-- output--- {1, 2, 20, 69, 7, 25, 11, 47}

POP  in set

a={20,25,47,69}
a.pop()
print(a)

--output --{20, 69, 47}

In this pop method it will delete one number randomly without any idea but 
if you want to delete particualr number use "remove"

REMOVE in set

a={20,25,47,69,33,39,41,63}
a.remove(20)
print(a)

--output--{33, 69, 39, 41, 47, 25, 63}

