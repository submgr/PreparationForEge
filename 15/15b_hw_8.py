def f(x, A):
    return ((x & 13 != 0) or (x & 42 != 0)) <= ((x & A != 0) or (x & 70 != 0))
   #return ((x & 13 != 0) or (x & 42 != 0)) <= ((x & A != 0) or (x & 70 != 0))


for A in range(1, 10000):
    if all(f(x, A) for x in range(1, 100000)):
        print(A)