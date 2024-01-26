class parent:
    a=10
    b=20


    def __init__(self,c,d):
        self.c=c
        self.d

class child(parent):

    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f
obt = child(4,5,7,6)