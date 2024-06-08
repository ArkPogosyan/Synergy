# сортировка пузырьком
import random

n = int(input())

arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)

print ('Без сортировки')
print(arr)
print('--------------------')

for i in range(n):
    flag = True;
    print(arr)
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            flag  = False
        if flag:
            break
    print('prohod', i, arr)
print('результат сортировки')
print(arr)