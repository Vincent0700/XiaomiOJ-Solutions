import sys

for line in sys.stdin:
    s = line.strip()
    if '+' in s:
        a, b = s.split('+')
        print(int(a) + int(b))
    elif '>' in s:
        a, b = s.split('>')
        print('Y' if int(a) > int(b) else 'N')
    elif '<' in s:
        a, b = s.split('<')
        print('Y' if int(a) < int(b) else 'N')
