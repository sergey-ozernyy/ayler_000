import time
start_time=time.time()
max_zn=0
max_posl=0
al=13
kol_al=2
i=1
while i < 1000000:
    if al%2==0:
        n=al//2
        if n!=1:
            al = n
            kol_al+=1
        else:
            if kol_al>max_zn:
                max_zn=kol_al
                max_posl=i
            kol_al=2
            i+=1
            al=i
            continue
    else:
        n=al*3+1
        if n!=1:
            al = n
            kol_al+=1
        else:
            if kol_al>max_zn:
               max_zn=kol_al
               max_posl=i
            kol_al=2
            i+=1
            al=i
            continue
print(max_zn,max_posl)






print(time.time()-start_time)
