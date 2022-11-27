for A in range(1, 1000):
    A_podoshel = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((x >= 23) or (2*x < y)) or (y * x < A)) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel == True:
        print(A)
