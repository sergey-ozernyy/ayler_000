#Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
import time
start_time = time.time()
a = []
d = []
delitel = []
b = 0
for i in range(10000,998002):
    if len(str(i)) == 5:
        b = list(str(i))
        if b[0] == b[-1] and b[1]==b[-2]:
            a.append(i)
    if len(str(i)) == 6:
        b = list(str(i))
        if b[0] == b[-1] and b[1]==b[-2] and b[2] == b[-3]:
            a.append(i)
for i in range(len(a)):
    for j in range(100,1000):
        if a[i] % j == 0:
            if len(str(a[i]//j))== 3 and len(str(j)) == 3:
                d.append(a[i])
                delitel.append(j)

print(max(d))
print("--- %s seconds ---" % (time.time() - start_time))
