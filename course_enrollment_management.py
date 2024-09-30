import sqlite3

# Function to create tables
def create_tables():
    conn = sqlite3.connect('course_enrollment.db')
    cursor = conn.cursor()

    # Create Student table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        StudentID VARCHAR(5) PRIMARY KEY,
        StudentName VARCHAR(100) NOT NULL
    );
    ''')

    # Create Course table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Course (
        CourseID VARCHAR(5) PRIMARY KEY,
        CourseName VARCHAR(100) NOT NULL,
        CreditHours INT NOT NULL CHECK (CreditHours > 0)
    );
    ''')

    # Create CourseEnrollment table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CourseEnrollment (
        CourseID VARCHAR(5),
        StudentID VARCHAR(5),
        Grade CHAR(2),
        PRIMARY KEY (CourseID, StudentID),
        FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
        FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
    );
    ''')

    conn.commit()
    conn.close()
    print("Tables created successfully!")

# Function to insert a student
def insert_student(student_id, student_name):
    conn = sqlite3.connect('course_enrollment.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Student (StudentID, StudentName) VALUES (?, ?);", (student_id, student_name))
    conn.commit()
    conn.close()
    print(f"Student {student_name} inserted successfully.")

# Function to insert a course
def insert_course(course_id, course_name, credit_hours):
    conn = sqlite3.connect('course_enrollment.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Course (CourseID, CourseName, CreditHours) VALUES (?, ?, ?);", (course_id, course_name, credit_hours))
    conn.commit()
    conn.close()
    print(f"Course {course_name} inserted successfully.")

# Function to enroll a student in a course
def enroll_student(course_id, student_id, grade):
    conn = sqlite3.connect('course_enrollment.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO CourseEnrollment (CourseID, StudentID, Grade) VALUES (?, ?, ?);", (course_id, student_id, grade))
    conn.commit()
    conn.close()
    print(f"Student {student_id} enrolled in course {course_id} with grade {grade}.")

# Function to delete a student from a course
def delete_student_from_course(student_id, course_id):
    conn = sqlite3.connect('course_enrollment.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM CourseEnrollment WHERE StudentID = ? AND CourseID = ?;', (student_id, course_id))
    conn.commit()
    conn.close()
    print(f"Student {student_id} removed from course {course_id}.")

# Function to delete a course
def delete_course(course_id):
    conn = sqlite3.connect('course_enrollment.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Course WHERE CourseID = ?;', (course_id,))
    conn.commit()
    conn.close()
    print(f"Course {course_id} removed successfully.")

# Function to update a student's grade
def update_student_grade(student_id, course_id, new_grade):
    conn = sqlite3.connect('course_enrollment.db')
    cursor = conn.cursor()
    
    cursor.execute('UPDATE CourseEnrollment SET Grade = ? WHERE StudentID = ? AND CourseID = ?;', (new_grade, student_id, course_id))
    conn.commit()
    conn.close()
    print(f"Grade updated for student {student_id} in course {course_id}.")

# Function to display all students
def display_all_students():
    conn = sqlite3.connect('course_enrollment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student;")
    results = cursor.fetchall()
    conn.close()
    print("\nCurrent Students:")
    for student in results:
        print(f"Student ID: {student[0]}, Student Name: {student[1]}")

# Function to display all courses
def display_all_courses():
    conn = sqlite3.connect('course_enrollment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Course;")
    results = cursor.fetchall()
    conn.close()
    print("\nCurrent Courses:")
    for course in results:
        print(f"Course ID: {course[0]}, Course Name: {course[1]}, Credit Hours: {course[2]}")

# Function to display all enrollments
def display_all_enrollments():
    conn = sqlite3.connect('course_enrollment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CourseEnrollment;")
    results = cursor.fetchall()
    conn.close()
    print("\nCurrent Enrollments:")
    for enrollment in results:
        print(f"Course ID: {enrollment[0]}, Student ID: {enrollment[1]}, Grade: {enrollment[2]}")

# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. View All Enrollments")
    print("2. View All Students")
    print("3. View All Courses")
    print("4. Insert Student")
    print("5. Insert Course")
    print("6. Enroll Student in Course")
    print("7. Update Student Grade")
    print("8. Delete Student from Course")
    print("9. Delete Course")
    print("10. Exit")

# Main function to run the program
def main():
    create_tables()  # Create tables if they don't exist
    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            display_all_enrollments()

        elif choice == '2':
            display_all_students()

        elif choice == '3':
            display_all_courses()

        elif choice == '4':
            student_id = input("Enter Student ID (e.g., S001): ")
            student_name = input("Enter Student Name: ")
            insert_student(student_id, student_name)

        elif choice == '5':
            course_id = input("Enter Course ID (e.g., C001): ")
            course_name = input("Enter Course Name: ")
            credit_hours = int(input("Enter Credit Hours: "))
            insert_course(course_id, course_name, credit_hours)

        elif choice == '6':
            course_id = input("Enter Course ID (e.g., C001): ")
            student_id = input("Enter Student ID (e.g., S001): ")
            grade = input("Enter Grade: ")
            enroll_student(course_id, student_id, grade)

        elif choice == '7':
            student_id = input("Enter Student ID (e.g., S001): ")
            course_id = input("Enter Course ID (e.g., C001): ")
            new_grade = input("Enter New Grade: ")
            update_student_grade(student_id, course_id, new_grade)

        elif choice == '8':
            student_id = input("Enter Student ID (e.g., S001): ")
            course_id = input("Enter Course ID (e.g., C001): ")
            delete_student_from_course(student_id, course_id)

        elif choice == '9':
            course_id = input("Enter Course ID to remove (e.g., C001): ")
            delete_course(course_id)

        elif choice == '10':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
