#student record display

name = input("enter the student's name: ")
roll_no = int(input("enter the student's roll no: "))
age = int(input("enter the age of the student: "))
marks1 = float(input("enter marks of maths: "))
marks2 = float(input("enter the marks of english: "))
marks3 = float(input("enter marks of science: "))
print("Name: ",name)
print("Roll no: ",roll_no)
print("age: ",age)
print("Maths: ",marks1)
print("English: ",marks2)
print("Science: ",marks3)
total_marks = marks1 + marks2 + marks3 
print("total marks: ",total_marks,"/300")
average = total_marks/3
print("Average: ",average)
percentage = total_marks/300*100
print("Percentage: ",percentage)
