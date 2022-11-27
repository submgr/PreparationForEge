for A in range(1, 1000):
    A_podoshel = True
    for x in range(0, 100):
        for y in range(0, 100):
            if ((31 - 2*y + 65 != 0) or (A < x) or (A < y)) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel == True:
        print(A)