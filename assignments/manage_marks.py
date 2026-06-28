def manage_marks():
    marks = []
    for i in range(5):
        try:
            mark = float(input(f"Enter mark {i+1}: "))
            marks.append(mark)
        except ValueError:
            print("Invalid input! Numeric only.")
            return
    
    print("Marks:", marks)
    print("Average:", sum(marks)/len(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
    
    marks.sort(reverse=True)
    print("Sorted Desc:", marks)

manage_marks()