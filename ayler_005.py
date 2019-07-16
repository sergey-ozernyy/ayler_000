#Какое самое маленькое число делится нацело на все числа от 1 до 20?
from functools import reduce
import time
start_time = time.time()
a = [11,12,13,14,15,16,17,18,19,20]
mn = [1]
nom = []
b = 0
b_max=0
x=[]
def somn(x):
    while reduce(lambda x, y: x*y, mn) != a:
        for i in range(2, x+1):
            if x%i == 0:
                mn.append(i)
                if x/i !=1:
                    somn(int(x/i))
                return(mn)
    return(mn) 
for i in range(10):
    nom.append(somn(a[i]))
    mn=[1]
print(nom)

for y in range(0,21):
    b_max=0
    for i in range(0,10):
        b=0
        for j in range(0,len(nom[i])):
            if nom[i][j] == y:
                b = b+1
        if b_max<b:
            b_max=b
    if y**b_max>1:
        x.append(y**b_max)
    
print(reduce(lambda q, w: q*w, x))
print("--- %s seconds ---" % (time.time() - start_time))   
