def toggle():
    a=(input("enter string"))
    i=0
    out=''
    while i <len(a):
        if 'a'<=a[i]<='z':
            out+=chr(ord(a[i])-32)
        elif 'A'<=a[i]<='Z':
            out+=chr(ord(a[i])+32)
        else:
            out+=a[i]
        i+=1
    return out
print(toggle())