num_lst = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')



answer, num = input().split(' ')
num = int(num)
answer = list(answer)
sum = 0


for idx, n in enumerate(answer):
    sum += num_lst.index(n) * (num**(len(answer)-idx-1))
    

print(sum)