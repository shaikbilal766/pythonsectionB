def  sum_of_even(num):
    if len(str(num)) == 6:
        out=0
        for i in str(num): 
            if int(i)%2==0:
                out+int(i)
    return out
print(sum_of_even(356557))

    