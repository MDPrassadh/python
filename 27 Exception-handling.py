'''
When an error occurs python will normally stop and generate an error message.
these exceptions can be handled using try statement....is called exception handling or error handling

b = 10
print(c)
'''

# this the error 

try :
    print(c)  # risky code
except :
    print( "Error" )
else :
    print( "No Error" )
finally :
    print("Always")
    
    #--output----Error
              # Always
              
try :
    print('c')  # risky code
except :
    print( "Error" )
else :
    print( "No Error" )
finally :
    print("Always")
    
# c
# no error
# always


try :

    print('c'+85)
except TypeError:
    print('TypeError')
except ValueError:
    print('Value Error')
    
    
    #  Always   
    #  TypeError