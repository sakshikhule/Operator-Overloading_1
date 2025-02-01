class Distance: 
    def __init__(self,km=0,m=0,cm=0): 
        self.km = km 
        self.m = m 
        self.cm = cm 
    def __add__(self,a):
    return Distance(self.km + a.km, self.m + a.m, self.cm + a.cm) 
    def __sub__(self,a): 
    return Distance(self.km - a.km, self.m - a.m, self.cm - a.cm) 
    def __str__(self): 
    return f"calculator obj: \nKm: {self.km}\nMeter: {self.m}\nCm: {self.cm}" 
    def __del__(self): 
    print("Destructor called!") 
    
c1 = Distance(2,7,5) 
c2 = Distance(4,9,6) 
res = c2 + c1  
print("Distance",res) 
res = c2 - c1 
print("Distance",res)
