import sys

N, L = map(int, sys.stdin.readline().split()) 
now = 0 # 현재 위치
answer = 0 

for _ in range(N):
    d, r, g = map(int, sys.stdin.readline().split()) # 신호등 위치, 빨간불, 초록불

    answer += (d - now) # 신호등 위치 - 현재 위치
    now = d # 현재 위치 갱신

    if answer % (r + g) <= r: # 경과시간 % (빨간불 + 초록불)이 빨간불 이하면 대기해야함
        answer += (r - (answer % (r + g))) # 대기시간 더하기

answer += (L - now) # 반복문을 돌고나면 신호등이 없는 도로의 길이를 더해야함.
print(answer)