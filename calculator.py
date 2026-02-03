def add(a , b):
    return a + b

def sub(a , b):
    return a - b

def multiply(a,b):
    """multiply two numbers"""
    return a*b

def safe_divide(a, b):
    if b == 0:
        return "Error: cant be divide by 0 "
    return a / b
