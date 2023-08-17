# n = int(input()) -> 시간초과

import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    command = sys.stdin.readline().split()
    # 1번 명령
    if command[0] == 'push':
        stack.append(command[1]) # command[0](push), 입력값 command[1]값을 넣어라  
    # 2번 명령
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # 3번 명령
    elif command[0] == 'size':
        print(len(stack))

    # 4번 명령
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    # 5번 명령
    elif command[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
