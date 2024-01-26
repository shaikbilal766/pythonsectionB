def fact2():
    a=int(input("enter a first number"))
    out=1
    for i in range(1,a+1):
        out=out*i
    print(out)
fact2()