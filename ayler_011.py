#Сначала преобразуем матрицу, чтобы можно было нормально работать с ее значениями
#Каково наибольшее произведение четырех подряд идущих чисел в таблице 20×20,
#расположенных в любом направлении (вверх, вниз, вправо, влево или по диагонали)?
def load_matr(file_name):
    mat=[]
    for i in open(file_name):
        i=str(i).split(' ')
        i[-1] = i[-1][:-1]
        for j in range(0,len(i)):
            if i[j][0] == '0':
                i[j] = i[j][1:]
            i[j] = int(i[j])
        mat.append(list(i))
    return mat
mat=load_matr('a.txt')
max_p=0
for i in range(20):
    for j in range(17):
        if (mat[i][j]*mat[i][j+1]*mat[i][j+2]*mat[i][j+3])>max_p:
            max_p=(mat[i][j]*mat[i][j+1]*mat[i][j+2]*mat[i][j+3])
            m1,m2,m3,m4=mat[i][j],mat[i][j+1],mat[i][j+2],mat[i][j+3]
            
for j in range(17):
    for i in range(20):
        if (mat[i][j]*mat[i][j+1]*mat[i][j+2]*mat[i][j+3])>max_p:
            max_p=(mat[i][j]*mat[i][j+1]*mat[i][j+2]*mat[i][j+3])
            m1,m2,m3,m4=mat[i][j],mat[i][j+1],mat[i][j+2],mat[i][j+3]

for i in range(17):
    for j in range(17):
        if (mat[i][j+3]*mat[i+1][j+2]*mat[i+2][j+1]*mat[i+3][j])>max_p:
            max_p=(mat[i][j+3]*mat[i+1][j+2]*mat[i+2][j+1]*mat[i+3][j])
            m1,m2,m3,m4=mat[i][j+3],mat[i+1][j+2],mat[i+2][j+1],mat[i+3][j]         



print(m1,m2,m3,m4)
print(mat)
print(max_p)
print(type(mat[0][0]))
