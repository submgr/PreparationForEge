def f(x, A):
    return not((((x & 11 != 0) <= (x & 21 == 0)) and ((x & 41 == 0) and (x & A == 0))))

for A in range(1, 100000):
    if all(f(x, A) for x in range(1, 10000)):
        print(A)
