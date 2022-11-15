for A in range (1, 1000000):
    A_podoshel = True
    for x in range (1, 1000000):
        if ((not(x%A == 0)) <= ((x%36 == 0) <= (not(x%81 == 0)))) == False:
            A_podoshel = False
            break
    if A_podoshel == True:
        print(A)
