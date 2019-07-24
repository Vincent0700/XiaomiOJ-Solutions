import sys
import math

cn = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']


def capitalize(num, padding=False):
    s = ''
    m1 = math.floor(num / 1000)  # 仟
    m2 = math.floor((num / 100) % 10)  # 佰
    m3 = math.floor((num / 10) % 10)  # 拾
    m4 = num % 10
    if m1 != 0:
        s += f'{cn[m1]}仟'
    elif padding:
        s += '零'
    if m2 != 0:
        s += f'{cn[m2]}佰'
    elif m1 != 0:
        s += '零'
    if m3 != 0:
        s += f'{cn[m3]}拾'
    elif m2 != 0:
        s += '零'
    if m4 != 0:
        s += cn[m4]
    elif m3 != 0:
        s += '零'
    if len(s) > 1 and s[-1] == '零':
        s = s[:-1]
    if len(s) == 0:
        s = '零'
    return s


for line in sys.stdin:
    num = int(line.strip())
    n1 = num % 10000  # 个
    n2 = math.floor((num / 10000) % 10000)  # 万
    n3 = math.floor((num / 100000000) % 10000)  # 亿
    ss = ''
    if n3 != 0:
        ss += f'{capitalize(n3)}亿'
    if n2 != 0:
        if n3 == 0:
            ss += f'{capitalize(n2)}万'
        else:
            ss += f'{capitalize(n2, True)}万'
    elif n3 != 0:
        ss += '零'
    if n1 != 0:
        if n2 == 0:
            ss += f'{capitalize(n1)}'
        else:
            ss += f'{capitalize(n1, True)}'
    elif n2 != 0:
        ss += '零'
    if len(ss) == 0:
        ss = '零'
    ss += '元整'
    print(ss)
