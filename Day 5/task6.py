# Task 6: Small Challenge
# Build a Student Marks Analyzer
# Ask for 5 marks, store in list, print average, max, min

def analyze_marks():
    marks = []  # Initialize an empty list to store marks
    for i in range(5):
        mark = int(input(f"Enter mark {i + 1}: "))  # Input marks from user
        marks.append(mark)  # Append each mark to the list
        avg = sum(marks) / len(marks)  # Calculate average. len gives number of elements in list
    print("Marks:", marks)  # Print the list of marks
    print("Average:", avg)
    print("Maximum:", max(marks))
    print("Minimum:", min(marks))
analyze_marks()  # Call the function to execute the marks analysis