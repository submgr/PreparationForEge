def f(x, A):
    return ((x & A != 0) <= ((x & 29 == 0) <= (x & 11 != 0)))

for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 10000)):
        print(A)
