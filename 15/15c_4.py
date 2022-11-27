for A in range(1, 1000):
    if all(((x > 42 or (y < x) or (3 * x < A))) for x in range(1, 10000) for y in range(1, 1000)):
        print(A)
        break