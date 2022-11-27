for A in range(1, 1000):
    if all(((((y + 5*x != 31) or (A > x - 2)) and (A < y + 37))) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
