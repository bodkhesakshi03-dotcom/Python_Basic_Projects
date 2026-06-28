class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []
    
    def add_mark(self, mark):
        try:
            mark = float(mark)
            self.marks_list.append(mark)
        except ValueError:
            print("Invalid mark! Must be numeric.")
    
     def get_average(self):
         return sum(self.marks_list)/len(self.marks_list) if self.marks_list else 0
    
     def display_info(self):
         print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks_list}, Avg: {self.get_average()}")

#  Demo
 s1 = Student("Sakshi", 9)
 s1.add_mark(100)
s1.add_mark("abc")  # invalid
s1.add_mark(100)
s1.display_info()