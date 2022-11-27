for A in range(1, 1000):
    A_podoshel = True
    for x in range(1, 100):
        for y in range(1, 100):
            if ((y - x != 5) or ((A > x*y) or (A > 3*y))) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel == True:
        print(A)
