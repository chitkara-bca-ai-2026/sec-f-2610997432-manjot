def process_student_result():
    print("---------------------------------------------")
    print("         SCHOOL RESULT PROCESSING            ")
    print("---------------------------------------------")
    student_name = input("Enter Student Name : ")
    roll_number = input("Enter Roll Number  : ")

    print("\n--- Enter Marks for 5 Subjects (0-100) ---")

    marks = []
    has_failed = False

    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    if mark < 40:
                        has_failed = True
                    break
                else:
                    print("Error: Marks must be between 0 and 100. Please try again.")
            except ValueError:
                print("Error: Invalid input. Please enter a numerical value.")
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    if has_failed:
        result = "FAIL"
        grade = "F"
        remarks = "Failed in one or more subjects"
    else:
        result = "PASS"
        if 90 <= percentage <= 100:
            grade = "A+"
            remarks = "Outstanding"
        elif 80 <= percentage < 90:
            grade = "A"
            remarks = "Excellent"
        elif 70 <= percentage < 80:
            grade = "B"
            remarks = "Very Good"
        elif 60 <= percentage < 70:
            grade = "C"
            remarks = "Good"
        elif 50 <= percentage < 60:
            grade = "D"
            remarks = "Satisfactory"
        elif 40 <= percentage < 50:
            grade = "E"
            remarks = "Pass"
        else:
            grade = "F"
            remarks = "Fail"
    print("\n")
    print("=============================================")
    print("            STUDENT REPORT CARD              ")
    print("=============================================")
    print(f"Student Name : {student_name}")
    print(f"Roll Number  : {roll_number}")
    print("=============================================")
    print(f"Total Marks  : {total_marks:.1f} / 500.0")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Result       : {result}")
    print(f"Grade        : {grade}")
    print(f"Remarks      : {remarks}")
    print("=============================================")


if __name__ == "__main__":
    process_student_result()
