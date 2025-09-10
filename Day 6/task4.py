# Task : Read line by line from a file

with open("notes.txt", "r") as file: # open file in read mode
    print("\n Reading line by line: ") # print message
    for line in file: # iterate through each line in the file maatlb ye keh raha hai k file k har line k liye
        print(line.strip()) # strip means remove any leading or trailing whitespace characters including new line character
    print("file read successfully") # print success message
# end of code