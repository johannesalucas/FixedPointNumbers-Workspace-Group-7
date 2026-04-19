from fixpoint_pkgFull import fixNum

def main_menu():
    while True:
        print("\n--- Fixed-Point Calculator (All Tasks) ---")
        print("1. Add two fixed-point numbers")
        print("2. Subtract two-fixed point numbers")
        print("3. Multiply two fixed-point numbers")
        print("4. Divide two fixed-point numbers")
        print("5. Comparison between two fixed-point numbers")
        print("6. [BONUS]: Exponential calculation (nth power)")
        print("7. Exit")
        
        choice = input("Select an option: ")
        if choice=='1': #Calling the 'add' function
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = str(input("  Fractional part (b): ")) #Working with it as string to deal with precision. This deals with a .05 and a .5 input
            p1=len(b1) #Passing this as the third argument; precision

            '''The process of taking the input and creating the fixed-point number is repeated across all operations, so we will just comment on it here. 
            We take the integral part and fractional part as separate inputs to allow for more control over the precision.
              The length of the fractional part is used to determine the precision, which is passed as an argument when creating the fixed-point number instance. 
              This ensures that the precision is consistent with the user's input and allows for accurate calculations across all operations.'''
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = str(input("  Fractional part (b): ")) 
            p2=len(b2)

            num1=fixNum(a1,int(b1),p1)
            num2=fixNum(a2,int(b2),p2)#Creating the fixed-point number instances using the inputs and precision
            result=num1+num2 #Using the overloaded '+' operator to perform the addition, which internally converts to float, performs the addition, and converts back to fixed-point
            print(f"{num1}+{num2}={result}")
            
        elif choice=='2': #Subtraction
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = str(input("  Fractional part (b): ")) #Working with it as string to deal with precision
            p1=len(b1)
            
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = str(input("  Fractional part (b): ")) 
            p2=len(b2)

            num1=fixNum(a1,int(b1),p1)
            num2=fixNum(a2,int(b2),p2)
            result=num1-num2 #Using the overloaded '-' operator to perform the subtraction, which internally converts to float, performs the subtraction, and converts back to fixed-point
            print(f"{num1}-{num2}={result}")
        
        elif choice == '3': #Multiplication
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = str(input("  Fractional part (b): ")) #Working with it as string to deal with precision
            p1=len(b1)
            
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = str(input("  Fractional part (b): ")) 
            p2=len(b2)

            num1=fixNum(a1,int(b1),p1)
            num2=fixNum(a2,int(b2),p2)
            result = num1*num2 #Using the overloaded '*' operator to perform the multiplication, which internally converts to float, performs the multiplication, and converts back to fixed-point
            print(f"\nResult: {num1} * {num2} = {result}")
            
        elif choice == '4': #Division
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = str(input("  Fractional part (b): ")) #Working with it as string to deal with precision
            p1=len(b1)
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = str(input("  Fractional part (b): ")) 
            p2=len(b2)

            num1=fixNum(a1,int(b1),p1)
            num2=fixNum(a2,int(b2),p2)
            result = num1/num2 #Using the overloaded '/' operator to perform the division, which internally converts to float, performs the division, and converts back to fixed-point. 
            #It also handles division by zero by printing an error message and returning None.
            print(f"\nResult: {num1} ÷ {num2} = {result}")
            
        elif choice == '5': #Comparison
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = str(input("  Fractional part (b): ")) #Working with it as string to deal with precision
            p1=len(b1)
            
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = str(input("  Fractional part (b): ")) 
            p2=len(b2)

            num1=fixNum(a1,int(b1),p1)
            num2=fixNum(a2,int(b2),p2)
            result = num1.compare(num2) #Using the 'compare' method to compare the two fixed-point numbers, which internally converts both to floats and returns a string indicating their relationship (greater than, less than, or equal to).
            print(result)
            
        elif choice=='6': #Exponential calculation (nth power): Bonus task.
            print("--Enter the base fixed point no:--")
            a=int(input("Integral part(a):"))
            b=str(input("Fractional part(b):"))
            p=len(b)
            base=fixNum(a,int(b),p) #Creating the fixed-point number instance for the base using the inputs and precision

            print("--Choose exponent type:--")
            print("A: Integer e.g -2,0,5")
            print("B: Fixed point no e.g 1.5") #Giving the user the option to choose between an integer exponent and a fixed-point exponent, which allows for more flexibility in the types of calculations that can be performed.
            
            exp_option=input("Select A or B:").upper() #Ensures the user's input is always in uppercase
            result=None #Initialize
            
            if exp_option=='A': #For integers
                n=int(input("Enter the value of n:"))
                result=base.power(n) #Calls the function directly
                
            elif exp_option=='B': #For fixed point
                print("Enter exponent fixed point:")
                ae=int(input("Integral part(a):"))
                be=str(input("Fractional part(b):"))
                pe=len(be)
                exp=fixNum(ae,int(be),pe) #Converts the exponent input into a fixed-point number instance, then does the calculation by calling the 'power method.
                result=base.power(exp)
                
            if result is not None: #Cleaning the print work
                print(f'Result:{result}')
            
        elif choice == '7': #Exit option
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
