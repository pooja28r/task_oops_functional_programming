import datetime

class RegistrationSystem:
    def __init__(self, max_students):
        self.MAX_STUDENTS = max_students
        self.students = []

    def register(self, roll_number, name, age):
        if len(self.students) >= self.MAX_STUDENTS:
            print(f"Error: Maximum number of students ({self.MAX_STUDENTS}) reached. Registration is closed.")
            return False

        current_date = datetime.datetime.now().date()
        REGISTRATION_START_DATE = datetime.date(2024, 4, 15)
        REGISTRATION_END_DATE = datetime.date(2024, 9, 15)
        if current_date < REGISTRATION_START_DATE or current_date > REGISTRATION_END_DATE:
            print("Error: Registration period has ended.")
            return False

        self.students.append({'roll_number': roll_number, 'name': name, 'age': age})
        print("Registration successful.")
        return True

    def show_registered_students(self):
        if not self.students:
            print("No students registered yet.")
            return

        print("Registered students:")
        for student in self.students:
            print(f"Roll Number: {student['roll_number']}, Name: {student['name']}, Age: {student['age']}")


def main():
    max_students = 5  # Set the maximum number of students
    registration_system = RegistrationSystem(max_students)

    while True:
        print("\nRegistration System Menu:")
        print("1. Register")
        print("2. Show Registered Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            roll_number = input("Enter student's roll number: ")
            name = input("Enter student's name: ")
            age = input("Enter student's age: ")
            registration_system.register(roll_number, name, age)
        elif choice == '2':
            registration_system.show_registered_students()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
