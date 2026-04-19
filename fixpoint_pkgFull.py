#fixnum_pkg.py
import math
class fixNum:
    def __init__(self, a,b,precision=None):
        '''Initializes the fixed-point number with integral part a, fractional part b, and precision (number of decimal places)'''
        self.a=int(a)
        self.b=int(b)
        #Storing the length of b to help with decimal reconstruction
        if precision is None:
            self.precision=len(str(b)) if b>0 else 2
        else:
            self.precision=precision #Storing the precision as an attribute to ensure consistency across operations.

    def to_float(self):
        '''Converts the internal representation to a float for calculation'''
        return self.a +(self.b/10**self.precision)
        

    def from_float(value,precision=2):
        '''Creates a fixNum instance from a float value, using the specified precision'''
        a=int(value)
        #(round..., 7) acts as a safety net to clean tiny binary errors at the 7th decimal place(safe choice)
        b=int(math.floor(round((value-a)*(10**precision),7)))
        return fixNum(a,b,precision)
#Using dunder methods
    def __add__(self,other): #Task 0
        '''Performs the addition task, converts both to floats to perform the math'''
        val1=self.to_float()
        val2=other.to_float()

        result=val1+val2

        return fixNum.from_float(result,self.precision)
        
    def __sub__(self,other): #Task 1
        '''Performs the subtraction task, converts both to floats to perform the math'''

        dif_val=self.to_float()-other.to_float()

        return fixNum.from_float(dif_val,self.precision)
        
    def __mul__(self,other): #Task 2(Our task)
        '''Performs the multiplication task, converts both to floats to perform the math'''
        val1=self.to_float()
        val2=other.to_float()

        raw_result=val1*val2
        #Return as a new fixed-point number
        
        return fixNum.from_float(raw_result,self.precision)
        
    def __truediv__(self,other): #Task 3
        '''Performs the division task, converts both to floats to perform the math'''
        val1=self.to_float()
        val2=other.to_float()
        #To account for division by 0 and not do the work:
        if val2==0:
            print("Error. Cannot divide by 0")
            return None
            
        raw_result=val1/val2
        return fixNum.from_float(raw_result,self.precision)
       
    def compare(self,other): #Task 4
        '''Compares two fixed-point numbers, returns -1 if self<other, 1 if self>other, and 0 if equal.
        Manually implemented instead of using dunder methods to practice the logic and return values as specified in the instructions.'''
        val1=self.to_float()
        val2=other.to_float()
        #Returning a series of values based on instructions:
        if val1 < val2:
            print("Second value is bigger")
            return -1
        elif val1 >val2:
            print("Second value is smaller")
            return 1
        else:
            print("Equal values")
            return 0
        

    def power(self,n): #Bonus task
        '''Raises the fixed-point number to the power of n, where n can be a positive/negative integer or another fixed-point number.'''
        if self.a==0 and self.b==0: #Accounting for when the value is 0 (Undefined)
            print("Error. Cannot raise 0 to a power")
            return None
        if isinstance(n,fixNum): #Accounts for both standard integers and complex fixed-point exponents
            exponent=n.to_float()
        else:
            exponent=n #Assume it is a positive/negative integer
        result_val=self.to_float()**exponent
            
        #Return as a new fixed point using the precision:
        return fixNum.from_float(result_val,self.precision)
                     

    def __str__(self):
        return f"{self.a}.{self.b:0{self.precision}d}" #This formatting ensures that the fractional part is always displayed with the correct number of decimal places, even if it has leading zeros.

    
#Testing the class with some examples:
if __name__=="__main__":
    num1=fixNum(12,48) #12.48
    num2=fixNum(2,16) #2.16
    print(f"num1: {num1}, num2: {num2}") #Expecting 12.48 and 2.16
    print(f"Addition: {num1} + {num2} = {num1+num2}") #Expecting 14.64
    print(f"Subtraction: {num1} - {num2} = {num1-num2}") #Expecting 10.32
    print(f"Multiplication: {num1} * {num2} = {num1*num2}") #Expecting 26.95
    print(f"Division: {num1} / {num2} = {num1/num2}") #Expecting 5.77
    print(f"Comparison: {num1} vs {num2} = {num1.compare(num2)}") #Expecting -1

    base=fixNum(2,16) #2.16
    exp_int=2 #Integer exponent
    exp_fix=fixNum(1,50) #1.50
    print(f"Base: {base}, Integer Exponent: {exp_int}, Fixed-point Exponent: {exp_fix}") #Expecting 2.16, 2, and 1.50 respectively
    print(f"Base raised to integer exponent: {base.power(exp_int)}") #Expecting 4.66
    print(f"Base raised to fixed-point exponent: {base.power(exp_fix)}") #Expecting 3.24