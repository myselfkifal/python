#Task 5
# Small Challenge: 
# Student record management system
# save student name and marks in a file

def save_students():
    with open("students.txt", "w") as f:   # "w" = write (creates file if not exist)
        for i in range(3):
            name = input("Enter student name: ")
            marks = input("Enter marks: ")
            f.write(f"{name},{marks}\n")
    print("✅ Students saved to file.")

def read_students():
    with open("students.txt", "r") as f:
        print("\n📖 Student Records:")
        for line in f:
            name, marks = line.strip().split(",")
            print(f"Name: {name}, Marks: {marks}")
    print("✅ Students read from file.")