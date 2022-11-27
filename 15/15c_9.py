for A in range(1, 1000):
    A_podoshel = True
    for x in range(1, 100):
        for y in range(1, 100):
            if (((x < 7) <= (x * y <= A)) and ((y * y < A) <= (y < 101))) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break

    if A_podoshel == True:
        print(A)