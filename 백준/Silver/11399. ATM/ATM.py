import sys
n = int(input())
peoples = list(map(int, sys.stdin.readline().split()))

peoples.sort()

answer = 0
for p in range(1,n+1):
    answer += sum(peoples[0:p])
print(answer)