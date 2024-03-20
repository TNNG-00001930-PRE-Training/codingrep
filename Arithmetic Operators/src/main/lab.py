
"""
    A class representing arithmetic operations.

     Let's say we're making a calculator app!
    
"""

def add_numbers( a, b):
        x=a+b
        return x

def subtract_numbers( a, b):
        x=a-b
        return x

def multiply_numbers( a, b):
        x=a*b
        return x
    

def divide_numbers( a, b):
    
        if b == 0:
            raise ValueError("Cannot divide by zero")
        else:
              x=a/b
        return x 

def modulus_numbers( a, b):
    
    if b == 0:
        raise ValueError("Cannot take modulus by zero")
    else:
          x=a%b
    return x 


    


       