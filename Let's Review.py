n = int(input()) 
for i in range(n):
    s = input()
    k = len(s)
    even = ''
    odd  = ''
    for t in range(k):
        if t%2 == 0:
            even += s[t]
        else:
            odd += s[t]
    print(even + ' ' + odd)