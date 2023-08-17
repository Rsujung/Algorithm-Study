import sys

n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    mean_n = int((n*0.15)+0.5)

    lst = []
    for i in range(n):
        lst.append(int(sys.stdin.readline()))


    lst2 = sorted(lst)
    lst2 = lst2[mean_n:n-mean_n]

    print(int(sum(lst2)/len(lst2)+0.5))