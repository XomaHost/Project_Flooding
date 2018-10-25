a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
    if a[i] == 'a':
        a.remove(a[i])
