def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Test the functions
print("Add:", add(5, 3))
print("Subtract:", subtract(10, 4))
print("Multiply:", multiply(2, 7))
print("Divide:", divide(10, 2))
