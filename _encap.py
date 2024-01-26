class parent1:
    __a=10
    b=20

    def __init__(self,c,d):
        self.__c=c
        self.d=d
    def __display(self):
        print (self.c,self.d)
        
obj=parent1(5,6)