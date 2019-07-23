import time
start_time=time.time()
def pr_ch_do_T(T):#Возвращает список простых чисел от 0 до Т
    T_l=list(range(T+1))#Список со значениями от 1 до T
    T_l[1]=0
    for i in T_l:
             if i > 0:
                 for j in range(i+i, T+1, i):
                     T_l[j]=0
    return slov(T_l,T)

def slov(T_l,T):#Словарь, где ключи это простые числа до Т, а их значения - None
    
    koef_mnoj_l=spisok_koef_pr_mnoj_do_obr(T_l,T)
    keys=list(range(len(T_l)))
    n=0
    mnoj_i_ih_kol=dict.fromkeys(keys)
    for i in mnoj_i_ih_kol:#Присваиваем каждому множителю число его повторений
        mnoj_i_ih_kol[i]=koef_mnoj_l[n]
        n+=1
    return koef_pr_mnoj_T(mnoj_i_ih_kol)

def koef_pr_mnoj_T(mnoj_i_ih_kol):
    koef_mnoj_l_nastoyshiy=[]
    for i in mnoj_i_ih_kol.values():#Выводим коэффициенты простых делителей
        if i > 0:
            koef_mnoj_l_nastoyshiy.append(i)
    return chislo_del(koef_mnoj_l_nastoyshiy)

def chislo_del(koef_mnoj_l_nastoyshiy):#Выводим число делителей
    ch_d=1
    for i in koef_mnoj_l_nastoyshiy:
        i+=1
        ch_d*=i
    return ch_d

def spisok_koef_pr_mnoj_do_obr(T_l,T):
    koef_mnoj=0
    koef_mnoj_l=[]
    for i in T_l:#Список коэффициентов простых множителей
        if i>0:
            while T%i==0:
                koef_mnoj+=1
                T=T//i
            else:
                koef_mnoj_l.append(koef_mnoj)
                koef_mnoj=0
        else:
            koef_mnoj=0
            koef_mnoj_l.append(koef_mnoj)
    return koef_mnoj_l

N=0
while True:
    N+=1
    T=int(1/2*N*(N+1))
    otvet=pr_ch_do_T(T)
    if otvet>500:
        print(T,otvet)
        break

print(time.time()-start_time)
