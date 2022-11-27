def f(x):
    return ((x & A != 0) <= (((x & 23 == 0) and (x & 8 == 0)) <= (x & 7 !=0)))

for A in range(1, 10000):
    if all(f(x) for x in range(1, 100000)):
        print(A)