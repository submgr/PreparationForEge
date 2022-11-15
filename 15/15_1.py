for A in range (1, 100000):
    A_podoshel = True
    for x in range (1, 1000000000000):
        if (((x % A == 0) and (x % 21 == 0)) <= (x % 18 == 0)) == False:
            A_podoshel = False
            break
    if A_podoshel == True:
        print(A)