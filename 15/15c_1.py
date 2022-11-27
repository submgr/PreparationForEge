for A in range(1, 1000):
    A_podoshel = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((15*x - 2*y + 37 != 0) or (A < x) or (A < y)) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel:
        print(A)
