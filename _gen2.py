def fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
out=fib(10)
print(list(out))
