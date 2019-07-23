import sys

for line in sys.stdin:
    arr = [int(i) for i in line.strip().split(",")]
    print(sorted(arr)[int((len(arr) - 1) / 2)])
