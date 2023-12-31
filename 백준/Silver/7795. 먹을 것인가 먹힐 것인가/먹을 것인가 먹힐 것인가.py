def binary_search(li, a):
    s, e = 0, len(li)-1 # 시작지점, 끝지점
    res = -1
    while s <= e:
        m = (s + e) // 2
        if li[m] < a:
            res = m
            s = m + 1
        else:
            e = m - 1
    return res # 작은수가없으면 -1 출력
    
    
for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (binary_search(B, a) + 1)
    print(cnt)