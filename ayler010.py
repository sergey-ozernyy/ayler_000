#Найдите сумму всех простых чисел меньше двух миллионов
import time
start_time=time.time()
def pr_ch(x):
    pr = list(range(x+1))
    pr[1]=0
    for i in pr:
        if i>0:
            for j in range(i+i, x, i):
                pr[j]=0     
    return sum(pr)
print(pr_ch(2000000))
print(time.time()-start_time)
