Q = list(range(8, 17 + 1))
P = list(range(3, 11 + 1))
A = list(range(1, 1000))
for x in range(1, 1000):
    if (((x in A) <= (x in P)) or (x in Q)) == False:
        A.remove(x)

print(A)

# 3 = 3
# 17 = 17
# 17 - 3 = 14
# ответ: 14