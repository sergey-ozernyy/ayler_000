#Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
import time
start_time=time.time()
a = sum([i**2 for i in range(1,101)])
b = sum([i for i in range(1,101)])**2
c = b-a
print(c)
print(time.time()-start_time)
