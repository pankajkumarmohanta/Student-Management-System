students = ['pankaj']

def show_menu():
    print("_" * 40)
    print("           STUDENT MANAGEMENT SYSTEM        ")
    print("_" * 40)
    print("\n1. Show student name")
    print("2. Add new student")
    print("3. Find student name")
    print("4. Remove student name ")
    print("5. Exist")

def show():
    print(students)

def new_stu():
    add_stu = input("Enter the student name want to add: ").lower()
    students.append(add_stu)
    print(f"{add_stu} added sucessfully in the list")

def find_stu():
    search_stu = input("Enter the student name want to find: ").lower()
    if search_stu in students:
        print(f"{search_stu} is in the list")
    else:
        print(f"{search_stu} not in the list")

def rem_stu():
    rem = input("Enter the student name want to remove: ").lower()
    if rem in students:
        students.remove(rem)
        print(f"{rem} removed sucessfully from the list")
    else:
        print(f"{rem} is not in the list")

while True:
    show_menu()
    choice = input("Please select a number between (1 to 5): ")
    if choice == '1':
        show()
    elif choice == '2':
        new_stu()
    elif choice == '3':
        find_stu()
    elif choice == '4':
        rem_stu()
    elif choice == '5':
        print("Thank You! for using Student management system")
        break
    else:
        print("Inviled number, Please enter the number between 1 to 5")