# Task: Append to a file

with open("notes.txt", "a") as file: # open file in append mode
    file.write("\nAdd o")
    file.write("\nAdd one more line at the end.")
    print("file appended successfully") # print success message
    file.close() # close the file
# end of code 