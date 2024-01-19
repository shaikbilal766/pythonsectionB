a=('messi')
out=''
for i in range(len(a)):
    if 1!=len(a)-1 and a[i]in a[i+1:]:
        out+=a[i]
print(out)
