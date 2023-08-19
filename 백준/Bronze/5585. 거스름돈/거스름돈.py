import sys
m = 1000 - int(sys.stdin.readline()) # 지불할 돈
c = 0 # 동전 개수

coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    c += m//coin 
    m %= coin 

print(c)