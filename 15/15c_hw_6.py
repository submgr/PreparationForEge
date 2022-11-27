for A in range(1, 1000):
    A_podoshel = True
    for x in range(0, 100):
        for y in range(0, 100):
            if (((y + 49 < A) and (23 - x < A)) or ((y + 2) * x > 99)) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel == True:
        print(A)