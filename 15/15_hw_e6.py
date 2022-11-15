def Del(n,m):
    return n%m == 0

for A in range(1, 10000):
    for x in range(1, 1000000):
        if (((Del(x, A)) and (Del(x, 36))) <= ((Del(x, 6)) and (Del(x, 120)))) == False:
            break
    else:
        print(A)