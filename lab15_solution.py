students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]}
}

print("=" * 50)
print("       STUDENT INFORMATION MANAGEMENT SYSTEM")
print("=" * 50)

while True:
    print()
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    print()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print()
        print("--- Enrolled Student Records ---")
        for roll, info in students.items():
            print(f"Roll No: {roll} | Name: {info['Name']} | Branch: {info['Branch']} | Sem: {info['Semester']} | Marks: {info['Marks']}")
        print("Total Enrolled Students:", len(students))

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        info = students.get(roll)
        if info:
            print()
            print(f"[FOUND] Record for Roll No {roll}:")
            print("   Name    :", info["Name"])
            print("   Branch  :", info["Branch"])
            print("   Semester:", info["Semester"])
            print("   Marks   :", info["Marks"])
        else:
            print(f"[ERROR] No record found for Roll No {roll}.")

    elif choice == "3":
        print()
        print("--- Register New Student ---")
        roll = input("Enter Roll Number: ")
        if roll in students:
            print(f"[ERROR] Roll No {roll} already exists.")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            semester = input("Enter Semester: ")
            print("Enter marks obtained in 3 subjects:")
            marks = []
            for i in range(1, 4):
                m = int(input(f"  Subject {i}: "))
                marks.append(m)
            students[roll] = {"Name": name, "Branch": branch, "Semester": semester, "Marks": marks}
            print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")
        if roll in students:
            print(f"Current details for {students[roll]['Name']} (Roll {roll}):")
            print(f"1. Branch: {students[roll]['Branch']} | 2. Semester: {students[roll]['Semester']}")
            field = input("Choose field to update (1 for Branch, 2 for Semester): ")
            if field == "1":
                students[roll]["Branch"] = input("Enter new branch: ")
                print(f"[SUCCESS] Branch updated to '{students[roll]['Branch']}'.")
            elif field == "2":
                students[roll]["Semester"] = input("Enter new semester: ")
                print(f"[SUCCESS] Semester updated to '{students[roll]['Semester']}'.")
            else:
                print("[ERROR] Invalid field choice.")
        else:
            print(f"[ERROR] No record found for Roll No {roll}.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")
        if roll in students:
            student = students[roll]
            total = sum(student["Marks"])
            average = total / len(student["Marks"])
            if average >= 40:
                status = "PASS"
            else:
                status = "FAIL"
            print()
            print("=" * 16, "ACADEMIC REPORT", "=" * 16)
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print("Subject Marks:", student["Marks"])
            print(f"Total Marks  : {total} / {len(student['Marks']) * 100}")
            print(f"Average Marks: {average:.2f}%")
            print("Final Result :", status)
            print("=" * 50)
        else:
            print(f"[ERROR] No record found for Roll No {roll}.")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")
        removed = students.pop(roll, None)
        if removed:
            print(f"[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"[ERROR] No record found for Roll No {roll}.")

    elif choice == "7":
        print()
        print("Thank you for using Student Information System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 7.")