
def student_database():
    students = {}
    
    while True:
        print("\nMenu:\n1. Add\n2. Search\n3. Display All\n4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            roll = input("Roll: ")
            name = input("Name: ")
            age = input("Age: ")
            city = input("City: ")
            students[roll] = {"name": name, "age": age, "city": city}
        
        elif choice == "2":
            roll = input("Enter roll: ")
            print(students.get(roll, "Not found"))
        
        elif choice == "3":
            for roll, info in students.items():
                print(f"Roll: {roll}, Info: {info}")
        
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

student_database()