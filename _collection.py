def fun(arg):
    if type(arg) in [str,tuple,set,dict,list]:
        return len(arg)
    else:
        return arg
b=[1,2,[4,5,6],'xyz',(4,1,2,3)]
print(list(map(fun,b)))