'''
child class or derived class

single Inheritance
Multilevel Inheritance
Multiple Inheriatance
Hierachicak Inheritance
'''
'''
# "SINGEL iNHERITANCE"   ----------one parent class and child class is called 

class Parent():
    def display(self):
        print("Iam parent")
        
class Child(Parent):
    def displayc(self):
        print("Iam child")

c=Child()
c.displayc()   # child method
c.display()   # parent method
              
#--Output---
# Iam child
# Iam parent
'''

'''
MULTILEVEL-INHERITANCE  ---------------- Level by level inheritance workout so is called as 

class GFather():
    def displaygf(self):
        print("Iam GFather")
class Father(GFather):
    def display(self):
        print("Iam Father")
class Child(Father):
    def displayc(self):
        print("Iam Child")
c=Child()
c.displayc()  # child method  Output--      Iam Child
c.display()  # father method   Output       Iam Father
c.displaygf()  # GFather Method  Output     Iam GFather
'''

'''
# Multiple -Inheritance ----Two parent classes and one child class 

class Father():
     def disaplyf(self):
      print("Iam Father")
class Mother():
    def displaym(self):
     print("Iam Mother")
class Child(Father,Mother):
    def displayc(self):
     print("Iam CHild") 
c=Child()
c.displayc()  # child method  Iam CHild
c.displaym()  # Mother method Iam Mother
c.disaplyf()  # father method Iam Father
'''


'''
# Hierachiral Inheritance:----Single parent class and multiple child classes
class Father():
    def displayf(self):
     print("Iam Head of the Family")
class Son(Father):
    def displays(self):
     print("Iam Son of this Family")
class Daughter(Father):
    def displayd(self):
     print("Iam the Little Princes of this Family")
c=Son()        # Son Object creation
c1=Daughter()  # Daughter Object creation
c.displays()   # Son Method  --------Iam Son of this Family
c.displayf()   # Father method-------Iam Head of the Family
c1.displayd()  # Daughter method-----Iam the Little Princes of this Family
c1.displayf()  # Father method-------Iam Head of the Family

'''

