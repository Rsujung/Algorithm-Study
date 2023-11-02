dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 
       'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0,'F':0.0 ,'P':None}

T = 20
score_1 = []
score_2 = []

for i in range(T):
    lst = input().split(' ')
    if lst[2] == 'P':
        continue
    else:
        hack = float(lst[1]) * float(dic[lst[2]])
        hap = float(lst[1])
        score_1.append(hack)
        score_2.append(hap)

f_score = sum(score_1) / sum(score_2)
print(round(f_score,6))