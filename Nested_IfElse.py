#Nested If-Else Statements, Taking example of multiple subjects and their marks of a student to determine the grade
Total_Subjects = 3
marks = []
for i in range(Total_Subjects):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total_marks = sum(marks)
average_marks = total_marks / Total_Subjects    

if average_marks >= 90:
    print("Grade: A")
elif average_marks >= 80:
    print("Grade: B")
elif average_marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

