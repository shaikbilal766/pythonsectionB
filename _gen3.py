
def binary(n):
    while n>0:
        yield n%2
        n=n//2
out=''
for i in binary(100):
    out=str(i)+out
print (out)
    