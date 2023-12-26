lst = []

for i in range(8):
    lst.append(int(input()))

five = []
score = 0

for i in range(5):
    score += max(lst)
    five.append(lst.index(max(lst)) + 1)
    lst[lst.index(max(lst))] = -1

five.sort()

print(score)
print(*five)