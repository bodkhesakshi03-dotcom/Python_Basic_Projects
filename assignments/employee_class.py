class Employee:
    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (dept, salary)
    
    def show_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.details[0]}, Salary: {self.details[1]}")

employees = {
    101: Employee(101, "Sakshi", "IT", 50000),
    102: Employee(102, "Amit", "HR", 45000),
    103: Employee(103, "Neha", "Finance", 60000)
}

for emp in employees.values():
    emp.show_details()
