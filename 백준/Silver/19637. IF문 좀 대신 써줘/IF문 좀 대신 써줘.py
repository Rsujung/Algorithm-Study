import sys

n, m = map(int, sys.stdin.readline().split())
powerList = []
nameList = []

for i in range(n):
    name, power = sys.stdin.readline().split()
    power = int(power)
    if powerList and powerList[-1] == power:  # 가장 처음 칭호만 저장해주기 위해
        continue
    powerList.append(power)
    nameList.append(name)


def binary_search(p):
    left = 0
    right = len(powerList) - 1
    while left <= right:
        mid = (left + right) // 2
        if p > powerList[mid]:
            left = mid + 1
        else:
            right = mid - 1
    print(nameList[right+1])


mList = []
for _ in range(m):
    p = int(sys.stdin.readline())
    binary_search(p)  # 이분탐색