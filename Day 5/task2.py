# Factorial using loop
def factorial(n):    # Function to calculate factorial
    result = 1 # Initialize result to 1
    for i in range(2, n + 1): # Loop from 2 to n
        result *= i # Multiply result by i in each iteration
    return result 
print("factorial of 5  is", factorial(5)) 
