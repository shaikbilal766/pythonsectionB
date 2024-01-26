class parent1:
    a=10
    b=20


    def __init__(self,c,d):
        self.c=c
        self.d=d
        print (self.c,self.d)

class parent2(parent1):
    b=20
    def __init__(self,c,d,e,f):
        super().__init__(c,d classmethod)
        self.e=e
        self.f=f
        print (self.e,self.f)
class child(parent2):
    c=30
    def __init__(self,c,d,e,f,g,h):
        super().__init__(c,d,e,f)
        self.g=g
        self.h=h
    
obj = child(4,5,7,6,5,8)