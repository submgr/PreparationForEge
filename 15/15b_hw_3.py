def f(x, A):
    return ((x & A != 0) <= (((x & 76 == 0) or (x & 45 == 0)) <= (x & 22 != 0)))


for A in range(1, 10000):
    if all(f(x, A) for x in range(1, 10000)):
        print(A)