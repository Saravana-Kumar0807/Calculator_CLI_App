def calculator() :
    while True :  
        print("\n---Simple CLI Calculator!---")
        print("1. Addition '+' ")
        print("2. Subtraction '-' ")
        print("3. Multiplication '*' ")
        print("4. Divition '/' " )
        print("5. Exit " )
        choice = input("\nEnter Your Choice :")
        if choice == '5':
            break
        try:
            num1 = float(input("Enter the number 1: "))
            num2 = float(input("Enter the number 2: "))
        except ValueError :
            print("Invalid input: Please enter numeric values!")
            continue          
        if choice == '1':
            print("\nResult :",num1+num2)
        elif choice == '2':
            print("\nResult :",num1-num2)
        elif choice == '3':
            print("\nResult : ",num1*num2)
        elif choice == '4':
            if num2 == 0:
                print("Zero Division Error!!! \n Try valid Operands.")
            else:  
                print("\nResult : ",num1/num2)
        else :
            print("Invalid Choice! \nSelect the above choices carefully(1-5).")        
calculator()

