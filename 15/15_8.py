def Del(n,m):
    return n%m == 0

for A in range(1, 10000):
    for x in range(1, 10000):
        if (Del(40, A) and (((not(Del(x, A))) and (Del(x, 54)) ) <= (not(Del(x, 72))))) == False:
            break
    else:
        print(A)