#Каков самый большой делитель числа 600851475143, являющийся простым числом?
pr_d = []
n = int(600851475143)
for i in range(1,775147):
    if n % i == 0:
        n = n/i
        pr_d.append(i)
print(pr_d)
print(max(pr_d))
