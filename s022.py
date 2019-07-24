import sys
import math

for line in sys.stdin:
    n = int(line.strip())
    row = math.ceil(math.sqrt(2 * n + 0.25) - 0.5)
    t = int(n - row * (row - 1) / 2)
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2]
    print(arr[(t - 1) % 16])
