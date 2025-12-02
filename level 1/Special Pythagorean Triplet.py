# Euclid's formula
    # m - n % 2 != 0
    # gcd =1
# a = k(m**2 - n**2)
# b = k(2mn)
# c = k(m**2 + n**2)
# m^2 + n^2 = 4m^2n^2 + m^4 + n^4 - 2m^2n^2
# k(m**2 + mn) = 500

from math import gcd

m = 2
flag = 1
while flag:
    for n in range(1, m):
        if gcd(n, m) == 1 and (m - n) % 2 == 1:
            k = 1
            m *= k
            n *= k
            while k * (m**2 + m * n) <= 500 :
                if  k * (m**2 + m * n) == 500:
                    print('founded', m,n, k)
                    print( k**3 * (m**2 + n**2) * (m**2 - n**2) * 2 * m * n)
                    flag = 0
                    break
                k += 1
    m += 1

# i = 2
# flag = 1
# while flag:
#     for j in range(i-1, 0, -1):
#         print(i,j)
#         if gcd(i, j) == 1 and (i - j) % 2 == 1:
#             a = i **2 - j **2
#             b = 2 * i * j
#             c = i **2 + j **2
#             k = 2
#             while a+b+c <= 1000:
#                 a *= k
#                 b *= k
#                 c *= k
#                 print(a+b+c )
#                 if (a+b+c) == 1000:
#                     print('founded',a, b, c)
#                     flag = 0
#                     break
#                 k +=1
#     i += 1

#ans = 31875000
