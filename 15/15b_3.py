for A in range(1, 1000):
    for x in range(1, 10000):
        if (((x & 21 != 0) and (x & 44 != 0)) <= ((x & A != 0) and (x & 21 != 0))) == False:
            break;
    else:
        print(A)