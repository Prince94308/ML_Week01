#Task-3
marks = float(input("Enter marks (0 - 100): "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
else:
    if marks >= 90:
        grade = 'A'
    elif marks >= 75:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    elif marks >= 40:
        grade = 'D'
    else:
        grade = 'Fail'

    print("Marks: {} -> Grade: {}".format(marks, grade))
