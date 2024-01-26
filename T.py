a=int(input('enter the 1st number'))
b=int(input('enter the 2nd number'))
if a>b:
    greater=a
else:
    greater=b
for i in range(1,greater+1):
    if a%i==0 and b%i==0:
        hcf=greater
print(hcf,end=' ')