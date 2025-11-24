import os

FILE = "students.txt"

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE, "a") as f:
        f.write(f"{roll},{name},{marks}\n")

    print("Student Added Successfully!\n")

def view_students():
    if not os.path.exists(FILE):
        print("No Records Found!\n")
        return

    print("\n---- STUDENT RECORDS ----\n")
    with open(FILE, "r") as f:
        for line in f:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Marks: {marks}")
    print()

def search_student():
    roll = input("Enter Roll No to Search: ")
    found = False

    if not os.path.exists(FILE):
        print("No Records Found!\n")
        return

    with open(FILE, "r") as f:
        for line in f:
            r, name, marks = line.strip().split(",")
            if r == roll:
                print(f"\nRecord Found: Roll={r}, Name={name}, Marks={marks}\n")
                found = True
                break

    if not found:
        print("Record Not Found!\n")

def delete_student():
    roll = input("Enter Roll No to Delete: ")

    if not os.path.exists(FILE):
        print("No Records Found!\n")
        return

    lines = []
    with open(FILE, "r") as f:
        lines = f.readlines()

    with open(FILE, "w") as f:
        for line in lines:
            r = line.split(",")[0]
            if r != roll:
                f.write(line)

    print("Record Deleted (if existed).\n")

while True:
    print("---- Student Record Management ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!\n")