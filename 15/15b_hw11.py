def f(x, A):
    return (((x & 54 == 0) or (x & 27 == 0)) <= ((x & 100 != 0) <= (x & A == 0)))


for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)