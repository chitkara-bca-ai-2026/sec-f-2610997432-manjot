# 1. Take student details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

print("\nEnter marks for 5 subjects (out of 100 each):")

marks = []

# 2. Input 5 subject marks using a loop with validation
for i in range(1, 6):
    while True:
        try:
            score = float(input(f"Enter marks for Subject {i}: "))
            if 0 <= score <= 100:
                marks.append(score)
                break
            else:
                print("Invalid input! Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Calculate total and percentage/average
total_marks = sum(marks)
average = total_marks / 5

# 3. Determine grade using nested if-elif conditions
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Print Report Card matching expected output structure
print("\n" + "=" * 40)
print("             REPORT CARD             ")
print("=" * 40)
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("-" * 40)
for i, m in enumerate(marks, start=1):
    print(f"Subject {i}    : {m}")
print("-" * 40)
print(f"Total Marks  : {total_marks} / 500")
print(f"Percentage   : {average:.2f}%")
print(f"Final Grade  : {grade}")
print("=" * 40)
