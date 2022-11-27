for A in range(1, 1000):
    A_podoshel = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((y + 42 < A) and (17 - x < A)) or ((y + 3) * x > 71)) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel == True:
        print(A)