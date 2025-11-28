from math import sqrt, ceil

def IsPrime(n):
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
factors = []
composites = []
fact = num
prime = 3

while prime <= ceil(sqrt(num)) :
    print(prime)
    if fact % 2 == 0:
        factors.append(2)
    elif fact % prime == 0 :
        factors.append(prime)
    prime += 2
# print(max(factors))

for factor in factors:
    # print(factor)
    if not(IsPrime(factor)):
        composites.append(factors[factors.index(factor)])
print(factors)
print(composites)
result = list(set(factors) - set(composites))
print(result)
print(max(result))
