R = list(range(12, 30 + 1))
Q = list(range(1, 15 + 1))
P = list(range(11, 20 + 1))

A = []

for x in range(1, 1000):
    if ((x in A) or (x in P)) or ((x in Q) <= (x in R)) == False:
        A.append(x)

print(A)

# 7 = 7
# 31 = 31

#Ответ: 24