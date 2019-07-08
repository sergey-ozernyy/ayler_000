#Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
a = [i for i in range(1,1000)]
b = []
for i in range(999):
    if a[i]%3 == 0 or a[i]%5 == 0:
      b.append(a[i])
print(sum(b))
