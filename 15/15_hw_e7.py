def Del(n,m):
    return n%m == 0

for A in range(1, 10000):
    for x in range(1, 1000 + 1):
        if ((Del(x, A) and (not(Del(x, 30)))) <= ((not(Del(x, 10))) or (not(Del(x, 7))))) == False:
            break
    else:
        print(A)