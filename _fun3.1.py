def toggle():
    a=(input("enter string"))
    i=0
    out=''
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        elif 'A'<=i<='Z':
            out+=chr(ord(i)+32)
        else:
            out+=i
    return out
print(toggle())