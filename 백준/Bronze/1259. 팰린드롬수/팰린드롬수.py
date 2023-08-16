while True:
    input1 = input()
    b = list(reversed(input1))
    input2 = int(''.join(b))

    if input1 == '0':
        break
    if int(input1) == input2:
        print('yes')
    else:
        print('no')