def f(x, A):
    return ((x & 58 == 0) or (x & 10 == 0)) <= (((x & 103 != 0) and (x & 17 != 0)) <= (x & A == 0))

for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)
