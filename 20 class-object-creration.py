'''
CLASS------------ is nothing but template 
class is blueprint of object creation
syntax:----

class classname():  # class definition

     # class body  or methods


blueprint means plan 

class -------------------------------object
car-----------------------------BMW,FERRARI
MOBILE--------------------------APPLE SMASUNG
BIKE--------------------------RE JAVA RX 100
STUDENT-----------------------RAJU MOHAN RANI

ONCE OBJECTED CREATED THEN MEMORY ALLOCATED TO CLASS


HERE VARIABLES AND METHODS EVERYTHING USING THROUGH OBJECT NAME

OBJECT-------------------PHYSICAL ENTITY
1 WE CAN CREATE ANY NUMBER OF OBJECTS FOR CLASS
CLASS ----------------------OBJECTS
CAR -------------------BMW,FERRARI,SUZUKI MARUTI THERE ARE OBJECTS

2 Memory is allocated when object is created
3 Object is an instance of a class

syntax-----------------------
objectname =classname()
4 using obeject we can access methods and variables of a class

syntax of ----------------

objectname.method()
objectname.variable()


Data 
function  both are called object


class a():
   # class body
v =a() # object creation
 here v is object....



'''

'''
#class is a blueprint of an object 
# object is a physical entity

class student():
    name = "prassadh"
    rollnumber = 15
    age = 25
    marks = 9.5
S1 = student()
print(S1.name)
print(S1.rollnumber)
print(S1.age)
print(S1.marks)

# output-----------
# prassadh
# 15 
# 25 
# 9.5
'''

class Python():    # class creation
    a=5
    def output(self):
        print(self.a)
b=Python()     # object creation
c=Python()
c.output()
b.output()
print(b.a)

#---output---
# 5
# 5
# 5

