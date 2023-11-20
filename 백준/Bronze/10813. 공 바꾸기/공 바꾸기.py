N, M = map(int, input().split(' '))

ball = []
for i in range(1,N+1):
    ball.append(i)

tmp = 0

for i in range(M):
    num1, num2 = map(int,input().split(' '))
    tmp = ball[num1-1]
    ball[num1-1] = ball[num2-1]
    ball[num2-1] = tmp


for i in range(N):
    print(ball[i], end=' ')