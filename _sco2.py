
def fun(s1, s2):
    out =0
    if len(s1)==len(s2):
        for i, j in zip(s1, s2):
            if i!=j:
                out += 1
        return out
    return 'not string'
print(fun('lip','pil'))