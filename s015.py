import sys

for line in sys.stdin:
    arr = [int(i) for i in line.strip().split(',')]
    length = len(arr)
    tmp = {}
    for i in range(length):
        for j in range(length):
            a = arr[i]
            b = arr[j]
            c = -(a + b)
            if i != j and c in arr:
                k = arr.index(c)
                if k != i and k != j:
                    tmp[','.join([str(i) for i in sorted([a, b, c])])] = 1
    print(len(tmp))
