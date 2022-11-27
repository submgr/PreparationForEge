def f(x, A):
    return ((x & 14 == 0) or (x & 32 == 0) or (x & A != 0))

for A in range(1, 10000):
    if(all(f(x, A) for x in range(1, 100000))):
        print(A)