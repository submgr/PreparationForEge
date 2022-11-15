for A in range(1, 1000000):
    for x in range(1, 1000000):
        if (((x % 48 == 0) or (x%72 == 0)) <= (x%A == 0)) == False:
            break;
    else:
        print(A)
print("end")