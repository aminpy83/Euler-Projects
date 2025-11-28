def IsPrime(n):
    for i in range(2, n// 2+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
factors = []
composites = []
fact = num
prime = 3

while prime <= num // 2 + 1 :
    print(prime)
    if IsPrime(prime):
        factors.append(prime)
    if fact % 2 == 0:
        factors.append(2)
    elif fact % prime == 0 and IsPrime(prime):
        factors.append(prime)
    prime += 2
print(max(factors))

# for factor in factors:
#     print(factor)
#     if not(IsPrime(factor)):
#         composites.append(factors[factors.index(factor)])
# print(factors)
# print(composites)
# result = list(set(factors) - set(composites))
# print(max(result))
