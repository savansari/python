class MathDojo:
    def __init__(self):
        self.result=0
    def add(self, a, *args):
        self.result+=a
        for e in args:
            self.result+=e
        return self
    
    def subtract(self, a, *args):
        self.result-=a
        for e in args:
            self.result-=e
        return self

md=MathDojo()
x=md.add(2).add(2,5,1).subtract(3,2).result
print("\nResult = ",x)

x=md.add(2).add(2,5,1).subtract(3,2,10).result
print("\nResult = ",x)

x=md.add(2).add(0).subtract(3,2).result
print("\nResult = ",x)