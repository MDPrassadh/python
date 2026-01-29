control-statements---are -3 types
1 conditional statements
2 looping statements
3 jumping statements

1 conditional statements:---
    if
    else
    elif
    nested if
    
2 looping statements:--
    for
    while
    nested loops
    
3 jumiping loops:--
   pass
   continue
   break

EXPLANATIONS-----if -else
if      
        condition:
          "statements"
else    
        "statements"

-------  if-else-elif-----------------
if      
        condition:
          "statements"
else    
        condition:
        "statements"
elif
        "statements"


--------nested-if----means if within the if condition--for instance outer if will execute try to execute inner if 
condition first other wise directly got for else condition withou going for inner if conditon...

if       condition:
            "statements"---if this conditon true then only go for inner if conditon otherwise strightly got for outer else will print
        
        if  conditon:
               "statements"
               
        else 
             "statements"
             
else   
        "statements"

age = 50

if age >= 58:
    print("pension will get")
else:
    print("you will not get pension")

you will not get pension

---------------------------------------

age = 50 output--you will not get pention
if age > 58:
     print("pention will get")
elif age == 58:
     print("pention will get")
else:
    print("you will not get pention")



age = 60   #--out-put--pension will get
if age > 58:
    print("pension will get")
elif age == 58:
    print("pension will get")
else:
    print("you will not get pension")


age = 58   #--out-put--pension will try to apply in this year to get pention
if age > 58:
    print("pension will get")
elif age == 58:
    print("pension will try to apply in this year to get pention")
else:
    print("you will not get pension")


age = 50  #--output---you will not get pension

if age >= 58:
    print("pension will get")
else:
    print("you will not get pension")


NESTED IF----------------

if True:
    print("outer if")
    
    if True:
        print("inner if")
    else: 
        print("inner else")
else:
    print("outer else")
    
# output--outer if 
#         inner if

if True:
    print("outer if")
    
    if False:
        print("inner if")
    else: 
        print("inner else")
else:
    print("outer else")
    
outer if
inner else

if False:
    print("outer if")
    
    if False:
        print("inner if")
    else: 
        print("inner else")
else:
    print("outer else")
    
--output---outer else direct else without trying nested if conditon bcz of outer if condition fails that is the reason