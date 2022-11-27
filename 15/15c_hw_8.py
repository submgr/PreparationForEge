for A in range(1, 1000):
    A_podoshel = True
    for x in range(0, 100):
        for y in range(0, 100):
            if (((y + 14 * x != 47) or (A > x - 2)) and (A < y + 61)) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel == True:
        print(A)