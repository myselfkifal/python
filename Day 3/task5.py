# Small Challenge
# Phonebook using Dictionary
# ask user for name, save number, then show all contacts

phonebook ={}
for i in range(3): # Loop to add 3 contacts
    name = input("Enter name: ") # Ask user for name
    number = input("Enter number: ") # Ask user for number
    phonebook[name] = number # Save in dictionary
print("Phonebook:", phonebook) # Print all contacts