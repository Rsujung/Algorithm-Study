L,S = map(int, input().split())

listen = []
see = []
for i in range(L):
    listen.append(input())
for i in range(S):
    see.append(input())


# set() 형식에서는 &연산자로 묶으면 둘의 중복항목만 뽑힘
answer = list(set(listen)& set(see))
answer.sort()
print(len(answer))
for i in answer:
    print(i)
