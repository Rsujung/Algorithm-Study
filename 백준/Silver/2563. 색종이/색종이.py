import sys

rows = 100
cols = 100
arr = [[0 for j in range(cols)] for i in range(rows)]

n = int(input())
for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    for i in range(w,w+10):
        for j in range(h,h+10):
            arr[i][j] = 1
            
print(sum(sum(arr, [])))