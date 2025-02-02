import csv

FILE_NAME = "student_records.csv"

def initialize_file():
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["StudentID", "Name", "Subject", "Marks", "Grade"])
        
        writer.writerows([
            ["101", "Ram", "Math", "85", "A"],
            ["102", "Bob", "Science", "78", "B"],
            ["103", "Verma", "English", "92", "A"],
            ["104", "Rohan", "History", "76", "C"],
            ["105", "Mohan", "Math", "89", "A"],
        ])
        
    print("Dummy data initialized in the CSV file.")

def create_record():
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        subject = input("Enter Subject: ")
        marks = input("Enter Marks: ")
        grade = input("Enter Grade: ")
        writer.writerow([student_id, name, subject, marks, grade])
        print("Record added successfully!")

def read_all_records():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        print("\nStudent Records:")
        for row in reader:
            print(", ".join(row))
    print()

def search_record():
    student_id = input("Enter Student ID to search: ")
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_id:
                print("Record Found: ", ", ".join(row))
                return
    print("Record not found.")

def update_record():
    student_id = input("Enter Student ID to update: ")
    updated = False
    records = []
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            records.append(row)
    for i in range(len(records)):
        if records[i][0] == student_id:
            print("Current Record: ", ", ".join(records[i]))
            name = input("Enter new Name: ")
            subject = input("Enter new Subject: ")
            marks = input("Enter new Marks : ")
            grade = input("Enter new Grade : ")
            records[i] = [student_id, name, subject, marks, grade]
            updated = True
            print("Record updated successfully!")
            with open(FILE_NAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(records)
            break

    if updated==False:
            print("Record not found.")







def delete_record():
    student_id = input("Enter Student ID to delete: ")
    deleted = False
    records = []

    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            records.append(row)

    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(records)):
            if records[i][0] != student_id:
                writer.writerow(records[i])
                print("Record not found.")
            else:
                deleted = True
                print("Record deleted successfully!")
                print("abcs")





def main():
    initialize_file()
    while True:
        print("\nStudent Database Management System")
        
        print("1. Add Record")
        print("2. View All Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_record()
        elif choice == "2":
            read_all_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            update_record()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
