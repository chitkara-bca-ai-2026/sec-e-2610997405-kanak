# SCHOOL RESULT PROCESSING

print("=" * 40)
print("        SCHOOL RESULT PROCESSING")
print("=" * 40)

name = input("Enter Student Name : ")
roll = input("Enter Roll Number  : ")

print()
print("--- Enter Marks for 5 Subjects (0-100) ---")

total = 0
failed = False

for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    if marks < 0 or marks > 100:
        print("Error: Marks must be between 0 and 100.")
        exit()
    if marks < 40:
        failed = True
    total = total + marks

percentage = (total / 500) * 100

if failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remark = "Good"
    elif percentage >= 50:
        grade = "D"
        remark = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remark = "Pass"
    else:
        grade = "F"
        remark = "Fail"

print()
print("=" * 40)
print("           STUDENT REPORT CARD")
print("=" * 40)
print(f"  Student Name : {name}")
print(f"  Roll Number  : {roll}")
print("-" * 40)
print(f"  Total Marks  : {total} / 500.0")
print(f"  Percentage   : {percentage:.2f}%")
print(f"  Result       : {result}")
print(f"  Grade        : {grade}")
print(f"  Remarks      : {remark}")
print("=" * 40)