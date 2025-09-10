# Read from a file

with open("notes.txt", "r") as file: # open file in read mode
    content = file.read() # read the content of the file
    print(content) # print the content
    file.close() # close the file
    print("file read successfully") # print success message
    