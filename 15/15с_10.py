count = 0;
for A in range(0, 1000):
    A_podoshel = True
    for x in range(1, 100):
        for y in range(1, 100):
            if (((x > 34) <= (x * y + 9 * x >= A)) and ((y * x + y > A) <= (y >= 2))) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break

    if A_podoshel == True:
        count += 1

print(count)