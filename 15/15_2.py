for A in range (1, 1000000):
    A_podoshel = True
    for x in range (1, 1000000):
        if (((x % 45 == 0) and (not (x % 15 == 0))) <= (not (x % A == 0))) == False:
            A_podoshel = False
            break
    if A_podoshel == True:
        print(A)
