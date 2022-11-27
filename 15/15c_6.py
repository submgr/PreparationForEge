for A in range(1, 1000):
    A_podoshel = True
    for x in range(1, 100):
        for y in range(1, 100):
            if ((y + 5 * x < A) or (x - 3*y > 75)) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel ==True:
        print(A)