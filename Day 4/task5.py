# Small Challenge
# calcualator using functions
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b if b!= 0 else "Error! Division by zero."
print("________Calculator________")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition:", add(num1,num2))
print("Subtraction:", subtract(num1,num2))
print("Multiplication:", multiply(num1,num2))
print("Division:", divide(num1,num2))
# End of the code