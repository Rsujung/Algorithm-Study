T = int(input())
step = []

for i in range(T):
    step.append(int(input()))

#예외처리 
if T == 1 or T == 2:
  print(sum(step))
  exit()


d_b = [step[0], step[0]+step[1]] # 밟은 버전
d_ab = [step[0], step[1]] # 안밟은 버전


for i in range(2,T):
    d_b.append(step[i] + d_ab[i-1])
    d_ab.append(step[i] + max(d_b[i-2], d_ab[i-2]))

print(max(d_b[T-1], d_ab[T-1]))