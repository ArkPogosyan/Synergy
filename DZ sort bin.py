def miBin(n):
    if n == 0:
        return '0'
    first_ch = '1' if n  %  2 == 1 else  '0'
    rem = miBin(n//2) if n >1 else ''
    return  rem + first_ch

n = int(input())
print(miBin(n))

