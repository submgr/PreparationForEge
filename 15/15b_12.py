def f(x, A):
    return ((x & A != 0) <= ((x & 12 == 0) <= (x & 39 != 0)))

for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 10000)):
        print(A)
