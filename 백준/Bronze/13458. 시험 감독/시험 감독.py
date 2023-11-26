import math 

N = int(input())
lst = list(map(int, input().split(' ')))
B, C = map(int, input().split(' '))
sum = 0


for i in range(len(lst)):
    if lst[i] <= B:
        sum += 1
    else:
        base = ((lst[i] - B)//C)
        if base == 0:
            sum += 2 
        else:    
            if (lst[i] -B)%C != 0:
                sum+=base + 2
            else:
                sum+=base + 1
                
sum = math.ceil(sum)
print(sum)