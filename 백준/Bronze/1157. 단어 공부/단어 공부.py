from collections import Counter

str = input()
upper = str.upper()
dic = Counter(upper)
a = dic.most_common()


if len(a)>1 and a[0][1] == a[1][1]:
    print('?')
else:
    print(a[0][0].upper())