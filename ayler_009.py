#Существует только одна тройка Пифагора, для которой a + b + c = 1000.
#Найдите произведение abc.
import time
start_time=time.time()
def pif():
    for a in range(1,500):
        for b in range(1,500):
            for c in range(1,500):
                if a+b+c == 1000 and a**2+b**2==c**2 and a<b:
                    return(a*b*c,'--',(time.time()-start_time))
                    
                    
        
print(pif())
