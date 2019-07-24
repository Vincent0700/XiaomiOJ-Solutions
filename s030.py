import sys

for line in sys.stdin:
    print(int(bin(int(line.strip()))[2:].rjust(32, '0')[::-1], 2))
