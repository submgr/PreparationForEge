def f(x, A):
    return (((x & 41 != 0 ) and (x & 50 != 0)) <= ((x & A != 0) or (x & 76 != 0)))


for A in range(1, 10000):
    if all(f(x, A) for x in range(1, 100000)):
        print(A)