N = input()

if len(N)<2:
    new_N = '0'+N
else:
    new_N = N


cnt = 0
while True:
    a = new_N[0]
    b = new_N[1]
    c = int(a) + int(b)
    new_N = b + str(c)[-1] 
    cnt += 1
    if int(new_N) == int(N):
        break
        

print(cnt)