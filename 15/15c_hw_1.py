for A in range(1, 1000):
    A_podoshel = True
    for x in range(1, 100):
        for y in range(1, 100):
            if ((y - 17 * x < A) or (x > 96) or (y > 101)) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel == True:
        print(A)
        break