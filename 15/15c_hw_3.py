for A in range(1, 1000):
    A_podoshel = True
    for x in range(0, 100):
        for y in range(0, 100):
            if (((x >= 19) or (3*x < y)) or (y*x < A)) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel == True:
        print(A)