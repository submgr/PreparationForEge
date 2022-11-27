Q = list(range(12, 31 + 1))
P = list(range(7, 13 + 1))

A = list(range(1, 1000))

for x in range(1, 1000):
    if (((x in A) <= (x in P)) or (x in Q)) == False:
        A.remove(x)

print(A)

# 7 = 7
# 31 = 31

#Ответ: 24