# Python Basic (Loops with functions and lists)

# FIND MAXIMUM NUMBER IN A LIST

def find_max(numbers): # Function to find the maximum number in a list
    max_num = numbers[0] # Assume the first number is the maximum
    for num in numbers: # Iterate through each number in the list
        if num > max_num: # If the current number is greater than the current maximum
            max_num = num # Update the maximum number
    return max_num # Return the maximum number found

num = [10,20,200,56,2]
print("list:", num) # Print the list of numbers
print("Maximum: ",find_max(num)) # Print the maximum number found in the list


# FIND MINIMUM NUMBER IN A LIST
def find_min(numbers): # Function to find the minimum number in a list
    min_num = numbers[0] # Assume the first number is the minimum
    for num in numbers: # Iterate through each number in the list
        if num < min_num: # If the current number is less than the current minimum
            min_num = num # Update the minimum number
    return min_num # Return the minimum number found

num = [10,20,200,56,2]
print("list:", num) # Print the list of numbers
print("Minimum: ",find_min(num)) # Print the minimum number found in the list
