def Del(n, m):
    return n % m == 0;

for A in range(1, 10000):
    for x in range(1, 1000):
        if (Del(A, 25) and ((Del(x, 24) and Del(x, 75)) <= Del(x, A))) == False:
            break
    else:
        print(A)