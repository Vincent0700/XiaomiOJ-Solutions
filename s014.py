import sys

for line in sys.stdin:
    a, b = line.strip().split(' ')
    num = int(b)
    arr = [int(i) for i in a.split(',')]
    if len(arr) > num:
        print(arr[num])
    else:
        print(-1)
