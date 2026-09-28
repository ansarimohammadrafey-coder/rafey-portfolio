print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

print("\nEnter marks for 5 subjects:")

english = float(input("English: "))
python = float(input("Python: "))
database = float(input("Database Management: "))
maths = float(input("Mathematics: "))
computer = float(input("Computer Science: "))

total = english + python + database + maths + computer
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 35:
    grade = "E"
else:
    grade = "F"

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("\n===== Result =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)

print("==============================")