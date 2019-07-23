import sys

arr = [0, 1, 2]

for line in sys.stdin:
    num = int(line.strip())
    if len(arr) > num:
        print(arr[num])
    else:
        for i in range(len(arr), num + 1):
            arr.append(arr[i - 1] + arr[i - 2])
        print(arr[num])
