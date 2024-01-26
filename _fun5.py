def fact(a):
    if a==1:
        return True
    return a*fact(a-1)
print(fact(5))   