
from fixpoint_pkg import fixNum

def main_menu():
    while True:
        print("\n--- Fixed-Point Calculator (Task 2) ---")
        print("1. Multiply two fixed-point numbers")
        print("2. [BONUS]:Exponential calculation (nth power)")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            #First number, enter a and b for the int and decimal part
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = int(input("  Fractional part (b): "))
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = int(input("  Fractional part (b): "))
            
            num1 = fixNum(a1, b1)
            num2 = fixNum(a2, b2)
            
            result = num1.multiply(num2)
            print(f"\nResult: {num1} * {num2} = {result}")
            
        elif choice=='2':
            print("--Enter the base fixed point no:--")
            a=int(input("Integral part(a):"))
            b=int(input("Fractional part(b):"))
            base=fixNum(a,b)

            print("--Choose exponent type:--")
            print("A: Integer e.g -2,0,5")
            print("B: Fixed point no e.g 1.5")
            
            exp_option=input("Select A or B:").upper() #Ensures the user's input is always in uppercase
            result=None #Initialize
            
            if exp_option=='A': #For integers
                n=int(input("Enter the value of n:"))
                result=base.power(n)
                
            elif exp_option=='B': #For fixed point
                print("Enter exponent fixed point:")
                ae=int(input("Integral part(a):"))
                be=int(input("Fractional part(b):"))
                exp=fixNum(ae,be)
                result=base.power(exp)
                
            if result is not None: #Cleaning the print work
                print(f'Result:{result}')
            
        elif choice == '3':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please t|ry again.")

if __name__ == "__main__":
    main_menu()
