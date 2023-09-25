from collections import deque
import sys

c = int(sys.stdin.readline())
answer = []

def bfs(start, end):
    q = deque([(start, end, 0)])
    while q:
        start, end, cnt = q.popleft()
        if start == end:
            return cnt
        if start * 2 <= end + 3:
            q.append((start * 2, end + 3, cnt + 1))
        if start + 1 <= end:
            q.append((start + 1, end, cnt + 1))

for _ in range(c):
    s, t = map(int, input().split())
    answer.append(bfs(s, t))

print(*answer, sep="\n")