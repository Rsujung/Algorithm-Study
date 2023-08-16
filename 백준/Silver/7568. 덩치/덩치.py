n = int(input()) # 반복횟수
lsts = [] 

for i in range(n):
    w, h = map(int, input().split(' ')) # 몸무게와 키를 값으로 받고 정수형으로 변환
    lsts.append((w, h)) # 리스트에 추가

# 키, 몸무게 비교
for i in lsts: 
    rank = 1
    for j in lsts:
        if i[0] < j[0] and i[1]<j[1]: # 키랑 몸무게 둘 다 작으면
            rank += 1 # 등수 밀려남
    
    print(rank, end=" ")