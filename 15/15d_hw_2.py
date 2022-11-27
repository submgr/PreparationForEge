Q = list(range(23, 40 + 1))
P = list(range(7, 25 + 1))
#Пожалуйста, будь ОЧЕНЬ внимательным здесь!! вводи правильно конфигурации отрезков

A = []

for x in range(1, 1000):
    if (((x in P) and (not(x in Q))) <= (x in A)) == False:
        A.append(x)

print(A)

# 7 = 7
# 22 = 23
# 23 - 7 = 16
# Ответ: 16
