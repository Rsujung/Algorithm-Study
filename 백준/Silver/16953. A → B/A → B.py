a,b = map(int,input().split()) 
r = 1                               # 총 연산 횟수
while(b!=a): 
    r+=1
    temp = b
    if b%10 == 1:   # 결과에 끝자리가 1이면
        b//=10      # 1을 뗀다
    elif b%2 == 0:  # 결과값이 짝수면
        b//=2       # 2로 나눈 몫을 비교
    
    if temp == b:   # 끝이 1로 끝나지도 않고 짝수도 아니면 답이 없음
        print(-1)   # -1 출력
        break
else:
    print(r)