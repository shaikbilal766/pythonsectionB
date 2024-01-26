def string(st,char):
    i=0
    count=0
    while i<len(st):
        if st[i]==char:
            count+=1
        i+=1
    print(count) 
string('hdhdh','h',)