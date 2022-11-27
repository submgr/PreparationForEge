Q = list(range(12, 90 + 1))
P = list(range(10, 29 + 1))
A = list(range(1, 1000))
for x in range(1, 1000):
    if (((x in Q) <= (x in P)) <= (not(x in A))) == False:
        A.remove(x)

print(A)

# 30 = 29
# 90 = 90
# 90 - 30 = 60
# ответ: 60