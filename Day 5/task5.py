# Count vowels in a string

def count_vowels(s): # Function to count vowels in a string
    vowels = "aeoiuAEIOU" # Define vowels
    count = 0 # Initialize count to 0
    for char in s:
        if char in vowels: # Check if the character is a vowel
            count += 1 # Increment count if it is a vowel
    return count # Return the total count of vowels
string = "Zulkifal Khan"
print("String:", string) # Print the original string
print("Number of vowels:", count_vowels(string)) # Print the number of vowels in the string
