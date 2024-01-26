rows=int(input('enter the number'))
out=''
for i in range(rows):
    for j in range(rows):
        if j==i or j==0:
            out+=' '
        else:
            out+='*'
    out+='\n'
name = input('Enter the file name')
with open(f'{name}.txtq','w') as file:
    file.write(out)
