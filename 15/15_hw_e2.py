def Del(n,m):
    return n%m == 0

for A in range(1, 10000):
    for x in range(1, 100000):
        if (Del(x, A) <= ((not(Del(x, 14)) or (Del(x, 84))))) == False:
            break
    else:
        print(A)