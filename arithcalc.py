print("Arithmetic Calculator")
print("Select an operation")
print(" 1. Addition (+)")
print(" 2. Subtraction (-)")
print(" 3. Multiplication (*)")
print(" 4. Division (/)")

try:
    choice = int(input("Enter the choice (1/2/3/4):"))      
    
    if choice in (1,2,3,4):
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        
        if choice == 1:
            result = num1+num2
            print(f"result: {num1} + {num2} = {result}")
        
        elif choice == 2:
            result = num1-num2
            print(f"result: {num1} - {num2} = {result}")
            
        elif choice == 3:
            result = num1*num2
            print(f"result: {num1} * {num2} = {result}")
            
        elif choice == 4:
            if num2 == 0:
                print("Error: division by zero is not allowed")
            
            else:
                result = num1/num2
                print(f"result: {num1} / {num2} = {result}")
        
    else:
        print("Invalid choice. Please select valid operation.")
            
except ValueError:
    print("Invalid output! please select numbers only.")            
            
            
    

            