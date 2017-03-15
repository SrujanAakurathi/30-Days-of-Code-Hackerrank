n = bin(int(input()))
b = n[2:]
i = 0
j = 0
m = 0
k = []
while i < len(b):
    if int(b[i]) == 1:
        m += 1
        i += 1
    elif int(b[i]) == 0:
        i += 1
        k.insert(j, m)
        j += 1
        m = 0
    if i == len(b):
        j += 1
        k.insert(j, m)

print(max(k))