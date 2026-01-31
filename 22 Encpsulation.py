'''
wrapping of variables and methods into single unit is called Encapsulation

ex--- MPC 
      CEC            all groups are included in COLLEGE like that 
      HEC
      BIPC 

python Has Access Specifiers:

1 Public
2 Private__   #( double Underscore __ for Private access Specifier)
            # CUrrent class access only
3 Protected_  # (single underscore _ for Protected access apecifier)
              # current class and Inherited calss only remaing restricted...
              


class display():
     __a=5 # private access only current acccess
     _b=9  # Protected access only current and inherited
     
     print(__a)
     print(_b)
     
     # output--- #5
                 #9
                 

class display():
    def __init__(self,a,b):
        self. __a=a # privated
        self. _b=b  # protected
        
class demo(display):
    def output(self):
        print(self. _b)   # but Here __a is not acces due to it is private access specifier its only workout current method not different but _b workout 
                            #it is bcz of protected that to it is inherited class thats why ...
b=demo(5,6)
b.output()

#output---------
# 6



class display():
    def __init__(self,a,b):
        self. __a=a # privated
        self. _b=b  # protected
        
class demo(display):
    def output(self):
        print(self. __a)   # but Here __a is not acces due to it is private access specifier its only workout current method not different but _b workout 
                            #it is bcz of protected that to it is inherited class thats why ...
                            # Look at this Error mesage
                            # AttributeError: 'demo' object has no attribute '_demo__a'
b=demo(5,6)
b.output()

'''