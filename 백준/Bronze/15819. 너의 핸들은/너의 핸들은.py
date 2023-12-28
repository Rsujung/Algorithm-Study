n, i = map(int, input().split(' '))
lst = []
for _ in range(n):
    lst.append(input())

sort = sorted(lst)
print(sort[i-1])