for A in range(1, 1000):
    A_podoshel = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y - 15 *x < A) or (x > 99) or (y > 64)) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel == True:
        print(A)
