s = set()
for i in input('ВВедите последовательность: ').split():
    if i not in s:
        s.add(i)
        print('NO')
    else:
        print('YES')
