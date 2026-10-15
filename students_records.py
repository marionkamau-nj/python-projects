
# STUDENTS RECORDS MANAGER USING FILE HANDLING

# Open and create a file
with open("students.txt", "w") as file:
    print("File created and opened successfully.")

    # Collect first student's information
    student_name = input("Enter Student Name: ")
    reg_no = input("Enter Registration Number: ")
    course = input("Enter Course: ")
    year_of_study = input("Enter Year of Study: ")
    department = input("Enter Your Department: ")
    email = input("Enter Email Address: ")
    phone_no = input("Enter Phone Number: ")
    academic_year = input("Enter Your Academic Year: ")
    semester = input("Semester: ")
    county = input("County: ")

    while True:
        try:
            admission_year = int(input("Admission Year: "))
            break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    student_status = input("Student Status: ")

    # Save the first student's information
    file.write(f"Student Name: {student_name}\n")
    file.write(f"Registration Number: {reg_no}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Year of Study: {year_of_study}\n")
    file.write(f"Department: {department}\n")
    file.write(f"Email Address: {email}\n")
    file.write(f"Phone Number: {phone_no}\n")
    file.write(f"Academic Year: {academic_year}\n")
    file.write(f"Semester: {semester}\n")
    file.write(f"County: {county}\n")
    file.write(f"Admission Year: {admission_year}\n")
    file.write(f"Student Status: {student_status}\n")


# Append the second student's details
with open("students.txt", "a") as file:
    file.write("\n")

    # Collect second student's information
    student_name = input("Enter Student Name: ")
    reg_no = input("Enter Registration Number: ")
    course = input("Enter Course: ")
    year_of_study = input("Enter Year of Study: ")
    department = input("Enter Your Department: ")
    email = input("Enter Email Address: ")
    phone_no = input("Enter Phone Number: ")
    academic_year = input("Enter Your Academic Year: ")
    semester = input("Semester: ")
    county = input("County: ")

    while True:
        try:
            admission_year = int(input("Admission Year: "))
            break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    student_status = input("Student Status: ")

    # Save the second student's information
    file.write(f"Student Name: {student_name}\n")
    file.write(f"Registration Number: {reg_no}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Year of Study: {year_of_study}\n")
    file.write(f"Department: {department}\n")
    file.write(f"Email Address: {email}\n")
    file.write(f"Phone Number: {phone_no}\n")
    file.write(f"Academic Year: {academic_year}\n")
    file.write(f"Semester: {semester}\n")
    file.write(f"County: {county}\n")
    file.write(f"Admission Year: {admission_year}\n")
    file.write(f"Student Status: {student_status}\n")


# Read and display all saved student information
with open("students.txt", "r") as file:
    content = file.read()
    print("\n--- SAVED STUDENT RECORDS ---")
    print(content)
