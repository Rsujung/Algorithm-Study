from collections import Counter
import sys

n = sys.stdin.readline()
array = list(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
x = list(map(int, sys.stdin.readline().split()))

# Counter함수 리스트 안에 원소들이 몇번 등장했는지 세어 딕셔너리 형태로 반환해줌
cnt = Counter(array)

for i in range(len(x)):
    if x[i] in cnt:
        print(cnt[x[i]], end=' ')
    else:
        print(0, end=' ')