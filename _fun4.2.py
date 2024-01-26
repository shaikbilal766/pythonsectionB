def index(str):
    a='aeiouAEIOU'
    out=''
    for i in a:
        if i not in str:
            out+=i
    return out
print(index('hello world'))