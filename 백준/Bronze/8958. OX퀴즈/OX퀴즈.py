import sys
N = int(input())

for _ in range(N):
    lst = list(sys.stdin.readline())
    count = [0]*len(lst)
    cnt = 0
    for idx, i in enumerate(lst):
        if i == 'O':
            cnt += 1
            count[idx] = cnt
        else:
            cnt = 0
            count[idx] = cnt
    print(sum(count))