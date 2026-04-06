#fixpoint_pkgFull.py
import math
class fixNum:
    def __init__(self, a,b):
        self.a=int(a)
        self.b=int(b)
        #Storing the length of b to help with decimal reconstruction
        self.precision=len(str(b)) if b>0 else 2

    def to_float(self):
        '''Converts the internal representation to a float for calculation'''
        return self.a +(self.b/10**self.precision)

    def from_float(value,precision=2):
        #Creates a fixNum object from a float result
        a=int(value)
        ''' (round..., 7) acts as a safety net to clean tiny binary errors at the 7th decimal place(safe choice)'''
        b=int(math.floor(round((value-a)*(10**precision),7)))
        return fixNum(a,b)

    def add(self,other): #Task 0, taking an extra step:
        val1=self.to_float()
        val2=other.to_float()

        result=val1+val2

        return fixNum.from_float(result,self.precision)
        
    def subtract(self,other): #Task 1
        dif_val=self.to_float()-other.to_float()

        return fixNum.from_float(dif_val,self.precision)
        
    def multiply(self,other): #Task 2(Our task)
        #Performs the multiplication task, converts both to floats to perform the math
        val1=self.to_float()
        val2=other.to_float()

        raw_result=val1*val2
        #Return as a new fixed-point number
        
        return fixNum.from_float(raw_result,self.precision)
        
    def divide(self,other): #Task 3
        val1=self.to_float()
        val2=other.to_float()
        #To account for division by 0 and not do the work:
        if val2==0:
            print("Error. Cannot divide by 0")
            return None
            
        raw_result=val1/val2
        return fixNum.from_float(raw_result,self.precision)
        
    def compare(self,other): #Task 4
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
        return f"{self.a}.{self.b:0{self.precision}d}" #The 0 pads the integers to avoid confusion between 12.05 and 12.5 for example. 


    
