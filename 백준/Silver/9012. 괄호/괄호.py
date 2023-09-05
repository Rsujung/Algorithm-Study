import sys

t = int(input())
for _ in range(t):
    stk = []
    s = sys.stdin.readline()
    isVPS = True

    for ch in s:
        if ch == '(':
            stk.append('(')
        if ch == ')':
            if stk:
                stk.pop()
            elif not stk:
                isVPS = False
                break
    if not stk and isVPS:
        print('YES')
    elif stk or not isVPS:
        print('NO')