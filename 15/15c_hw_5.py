count = 0

for A in range(1, 1000):
    A_podoshel = True
    for x in range(0, 100):
        for y in range(0, 100):
            if (((x > 18) <= (x*y + 14*x >= A)) and ((y*x + y > A) <= (y>= 3))) == False:
                A_podoshel = False
                break
        if A_podoshel == False:
            break
    if A_podoshel == True:
        #print(A)
        count += 1

print(count)