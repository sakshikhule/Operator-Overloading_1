class Complex_Num: 
    def __init__(self,real=0,img=0): 
        self.real = real 
        self.img = img 
 
    def __add__(self,a): 
        return Complex_Num(self.real + a.real, self.img + a.img) 
     
    def __sub__(self,a): 
        return Complex_Num(self.real - a.real, self.img - a.img) 
     
    def __str__(self): 
        return f"calculator obj: {self.real} + {self.img}i" 
 
    def __del__(self): 
        print("Destructor called!") 
 
c1 = Complex_Num(2,7) 
c2 = Complex_Num(4,9) 
res = c1 + c2 
print("Complex number (+): ",res) 
res = c1 - c2 
print("Complex number (-): ",res)
