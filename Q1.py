# Task-1
matrix = [
    ["name", "sub1", "sub2", "sub3"],
    ["Rajnish", 89, 79, 67],
    ["Akshay", 90, 79, 98],
    ["Dipu", 91, 92, 93]
]

print(matrix)


for student in matrix[1:]:
    name = student[0]
    marks = student[1:]
    total = sum(marks)
    average = total / len(marks)
    
    print("Student: {}".format(name))
    print("  Total Marks: {}".format(total))
    print("  Average Marks: {:.2f}".format(average))
