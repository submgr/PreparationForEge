D = list(range(30, 45 + 1))

def Del(n, m):
    return n % m == 0

for A in range(1, 10000):
    for x in range(1, 10000):
        if (((not(Del(x, 6))) and x not in [45, 50, 55]) <= ((abs(x - 30) <= 5) <= (x in D)) or (x & A != 0)) == False:
            break
    else:
        print(A)

# 4 = 4
# 32 = 32
# 32 - 4 = 28
# Ответ: 28