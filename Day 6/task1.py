# Python Basics (File Handling)
# task: write a file

with open("notes.txt", "w") as file: # open file in write mode
    file.write("hello i am learning python") # write to file
    file.write("This is my Day 6 of python") # write to file

    print("file wtitten successfully") # print success message
    file.close() # close the file

# end of code
