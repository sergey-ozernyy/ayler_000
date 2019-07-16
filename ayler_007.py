#Какое число является 10001-ым простым числом?
import time
start_time=time.time()
b=[]
a=2
pr=[2]
while len(pr)!=10001:
    for i in pr:
        if a%i == 0:
            break  
    if a%i !=0:
        pr.append(a)
    a+=1
print(pr,pr[-1])
print(time.time()-start_time)
