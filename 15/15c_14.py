def Del(n, m):
    return n % m == 0

for A in range(1, 1000):
    if all(((Del(x, 2) <= (not(Del(x, 3)))) or (x + A >= 80)) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)