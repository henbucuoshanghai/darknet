import os
for i in os.listdir("../results/"):
    a=i.split('_')[-1]
    new="../results/"+a
    i="../results/"+i
    os.rename(i,new)
    
