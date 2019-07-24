import sys
import math

ops_rule = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}


def infix2postfix(exp_arr):
    expression = []
    ops = []
    for item in exp_arr:
        if item in ['+', '-', '*', '/']:
            while len(ops) >= 0:
                if len(ops) == 0:
                    ops.append(item)
                    break
                op = ops.pop()
                if ops_rule[item] > ops_rule[op]:
                    ops.append(op)
                    ops.append(item)
                    break
                else:
                    expression.append(op)
        else:
            expression.append(int(item))

    while len(ops) > 0:
        expression.append(ops.pop())

    return expression


def calc_postfix(exp):
    stack_value = []
    err = False
    for item in exp:
        if item in ['+', '-', '*', '/']:
            n2 = stack_value.pop()
            n1 = stack_value.pop()
            if item == '+':
                r = n1 + n2
            elif item == '-':
                r = n1 - n2
            elif item == '*':
                r = n1 * n2
            else:
                if n2 != 0:
                    r = n1 / n2
                else:
                    err = True
                    break
            stack_value.append(int(r))
        else:
            stack_value.append(int(item))

    return stack_value[0] if not err else None


for line in sys.stdin:
    arr = line.strip().split(' ')
    result = calc_postfix(infix2postfix(arr))
    if result is not None:
        print(math.floor(result))
    else:
        print('err')
