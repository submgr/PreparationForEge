def Del(n, m):
    return n % m == 0

for A in range(1, 10000):
    for x in range(1, 1000):
        if ((Del(x, 175) <= (not(Del(x, 25))) ) or (2 * x + A >= 1780)) == False:
            break;
    else:
        print(A)