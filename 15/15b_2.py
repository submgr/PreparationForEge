for A in range(1,1000):
    for x in range(1, 10000):
        if ((x & A !=0) <= ((x & 14 == 0) <= (x & 75 !=0))) == False:
            break
    else:
        print(A)