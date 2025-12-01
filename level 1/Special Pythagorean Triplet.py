# Euclid's formula
    # m - n % 2 != 0
    # gcd =1
# a = m**2 - n**2
# b = 2mn
# c = m**2 + n**2
from math import gcd

i = 2
flag = 1
while flag:
    for j in range(1, i):
        if gcd(i, j) == 1 and (i - j) % 2 == 1:
            a = i **2 - j **2
            b = 2 * i * j
            c = i **2 + j **2
            k = 2
            while a+b+c <= 1000:
                a *= k
                b *= k
                c *= k
                print(a+b+c )
                if (a+b+c) == 1000:
                    print('founded',a, b, c)
                    flag = 0
                    break
                k +=1
    if not flag:
        break
    i += 1
