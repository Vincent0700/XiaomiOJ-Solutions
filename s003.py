import sys

for line in sys.stdin:
    a, b = line.strip().split("-")
    print(int(a) - int(b))
