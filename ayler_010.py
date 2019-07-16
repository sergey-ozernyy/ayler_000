#Найдите сумму всех простых чисел меньше двух миллионов
import time
start_time=time.time()
def pr_ch(x):
    a=2
    pr=[2]
    while len(pr)!=x+1:
        for i in pr:
            if a%i == 0:
                break  
        if a%i !=0:
            pr.append(a)
        a+=1
    return pr
print(sum(pr_ch(200000)))
print(time.time()-start_time)
