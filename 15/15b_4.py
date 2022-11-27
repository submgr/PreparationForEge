def f(x):
    return (((x & 19 !=0) or (x & 49 != 0)) <= ((x & 21 == 0) <= (x & A != 0)))

b = []
for A in range(1, 1000):
    if all(f(x) for x in range (1, 10000)):
         print(A)