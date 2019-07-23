import sys

for line in sys.stdin:
    s1, s2 = line.strip().split(' ')
    arr = {}
    flag = True
    for c in s2:
        if c in arr:
            arr[c] += 1
        else:
            arr[c] = 1
    for c in s1:
        if c not in arr or arr[c] == 0:
            print('false')
            flag = False
            break
        else:
            arr[c] -= 1

    if flag:
        print('true')
