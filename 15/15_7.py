def Del(n,m):
    return n%m == 0

for A in range(1, 100000):
    for x in range(1, 1000000):
        if ((Del(A, 5)) and ((not(Del(2020, A))) <= ((Del(x, 1718)) <= Del(2021, A)))) == False:
            break;
    else:
        print(A)

print("finished.")