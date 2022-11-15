def Del(n,m):
    return n%m == 0

for A in range(1, 10000):
    for x in range(1, 1000 + 1):
        if ((Del(x, A) and Del(x, 33) ) and (Del(x, 11))) == True:
            break
    else:
        print(A)