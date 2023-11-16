a, b = map(int, input().split(' '))
n = int(input())
a_num = [int(x) for x in list(input().split(' '))]

sum = 0
for idx in range(n):
    sum += a_num[idx] * (a**(n-idx-1))

a = []
while sum:
    a.append(sum % b)
    sum//=b

for i in a[::-1]:    
    print(i, end=' ')