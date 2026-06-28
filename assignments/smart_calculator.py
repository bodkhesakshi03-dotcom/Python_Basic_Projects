
import math, random, time

def smart_calculator():
    history = {}
    
    while True:
        print("\nMenu:\n1. Arithmetic\n2. Scientific\n3. Random\n4. Store Result\n5. View History\n6. Exit")
        choice = input("Choice: ")
        
        try:
            if choice == "1":
                a = float(input("First: "))
                b = float(input("Second: "))
                op = input("Operation (+,-,*,/): ")
                if op == "+": result = a + b
                elif op == "-": result = a - b
                elif op == "*": result = a * b
                elif op == "/": result = a / b
                else: result = "Invalid"
                print("Result:", result)
            
            elif choice == "2":
                x = float(input("Enter number: "))
                print("Sqrt:", math.sqrt(x))
                print("Power:", math.pow(x, 2))
            
            elif choice == "3":
                print("Random:", random.randint(1, 100))
            
            elif choice == "4":
                res = input("Enter result: ")
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                history[timestamp] = res
                print("Stored!")
            
            elif choice == "5":
                for t, r in history.items():
                    print(f"{t}: {r}")
            
            elif choice == "6":
                break
            else:
                print("Invalid choice!")
        except Exception as e:
            print("Error:", e)

smart_calculator()

