class Calculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"square:  {self.n*self.n}")
    def cube(self):
        print(f"Cube:  {self.n*self.n*self.n}")

c=Calculator(2)
c.square()
c.cube()
