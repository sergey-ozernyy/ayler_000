import time
start_time=time.time()
l=''
for line in open('a_13.txt'):
    l+=line
l_list=l.split('\n')
l_int=map(int,l_list)
l_sum=sum(list(l_int))
l_l=''
for i in str(l_sum):
    l_l+=i
    if len(l_l)==10:
        print(l_l)
        break


print(time.time()-start_time)  
