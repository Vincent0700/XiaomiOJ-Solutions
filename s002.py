import sys

for line in sys.stdin:
    a = {}
    for i in line.strip().split():
        if i in a:
            a[i] += 1
        else:
            a[i] = 0
    for i in a:
        if a[i] == 0:
            print(i)
