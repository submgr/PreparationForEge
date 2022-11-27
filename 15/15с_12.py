for A in range(1, 1000):
    if all(((4*y - x < A) or (x >= 81) or (y >= 35)) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break