def Del(n,m):
    return n%m == 0

for A in range(1, 10000):
    for x in range(1, 1000000):
        if (Del(x, A) <= ((Del(x,7)) or (Del(x, 70)))) == False:
            break
    else:
        print(A)