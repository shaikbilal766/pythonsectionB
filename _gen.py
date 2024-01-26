def fun(a,b):
    
    yield a+b
    yield a*b
out=fun(3,2)
for i in out:

    print(i)

