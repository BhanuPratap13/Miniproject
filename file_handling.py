input_file_path = "C:\\Users\\bhanu\\OneDrive\\Documents\\student_data.txt"
output_file_path = "C:\\Users\\bhanu\\OneDrive\\Documents\\report_card.txt"

with open("C:\\Users\\bhanu\\OneDrive\\Documents\\student_data.txt", 'r') as file:
    lines = file.readlines()

report_card = ""
for idx, line in enumerate(lines):
    data = line.strip().split(',')
    student_id = idx + 1
    name = data[0]
    marks = list(map(int, data[1:]))
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

    if average_marks >= 90:
        grade = 'A'
    elif average_marks >= 80:
        grade = 'B'
    elif average_marks >= 70:
        grade = 'C'
    elif average_marks >= 60:
        grade = 'D'
    else:
        grade = 'F'

    report_card += f"ID: {student_id}\nName: {name}\nMarks: {', '.join(map(str, marks))}\nTotal Marks: {total_marks}\nAverage Marks: {average_marks:.2f}\nGrade: {grade}\n\n"

with open("C:\\Users\\bhanu\\OneDrive\\Documents\\report_card.txt", 'w') as file:
    file.write(report_card)