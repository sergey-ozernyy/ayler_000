#Найдите сумму всех четных элементов ряда Фибоначчи,
#которые не превышают четыре миллиона.
a = 1
b = 2
arr = []
arr_ch = []
while a&b <= 4000000:
    arr.append(a)
    arr.append(b)
    a = a + b
    b = b + a
for i in range(len(arr)):
    if arr[i]%2 == 0:
       arr_ch.append(arr[i])
print(sum(arr_ch))
