class Add:
    @staticmethod
    def add2(a,b):
        return a + b
    
    @staticmethod
    def add3(a,b,c):
        return a + b + c
class Sub:
    @staticmethod
    def sub2(a,b):
        return a - b
class Mul:
    @staticmethod
    def mul2(a,b,):
        return  a * b
class cal(Add,Sub,Mul):
    pass
obj=cal()
print(obj.add2(3,4))