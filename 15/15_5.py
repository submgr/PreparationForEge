for A in range(1, 100000):
    for x in range (1, 100000):
        if (((x%A == 0) and (x%16 == 0)) <= ((not(x%16 == 0)) or (x%24 == 0))) == False:
            break
    else:
        print(A)

print("finished.")