for A in range (1, 10000):
    for x in range (1, 100000):
        if ((x & 91 != 0) <= ((x & 23 == 0) <= (x & A != 0))) == False:
            break
    else:
        print(A)