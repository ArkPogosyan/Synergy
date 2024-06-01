import random
m = int(input('введите число m-:'))
n  = int(input('введите число n-:'))

matrix_1 = [[random.randint(1,11) for i in range (n)] for j in range(m)]
print('matrix_1', matrix_1)
matrix_2 = [[random.randint(1,11) for i in range(n)] for j in range(m)]
print('matrix_2', matrix_2)
for i in range(m):
    Result = [[matrix_1[i][j]+matrix_2[i][j] for j in range(len(matrix_1[0]))] for j in range(len(matrix_1[i]))]
print('Result', Result)   
