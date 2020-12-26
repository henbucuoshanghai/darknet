import os
f = open("a.txt","r") 
f_v=open("val.txt","w")
for i in f.readlines():
    i=i.replace("F:/MSCOCO",'.')
    f_v.writelines(i)
    print(i)
f.close()
f_v.close()
