def proizved(a, b):
    s = 0
    while b != 0:
        s = s + a
        b = b  - 1

    return s


a= int(input())
b= int(input())
print(proizved(a,b))
