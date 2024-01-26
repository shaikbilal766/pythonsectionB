import re
with open(r"C:\Users\administrator.MCA\Desktop\file.txt",'r+') as file:
    data=file.read()
    newdata=re.sub('_','+',data)
    file.seek(0)
    file.write(newdata  )