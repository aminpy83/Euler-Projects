from math import sqrt, ceil

def is_prime(n):
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
max_prime = 0
prime = 3
# factors = []

while prime <= ceil(sqrt(num)) :
    if num % 2 == 0:
        max_prime = prime
    elif num % prime == 0 and is_prime(prime):
        max_prime = prime
    prime += 2
print(max_prime)

# composites = []
# for factor in factors:
#     # print(factor)
#     if not(is_prime(factor)):
#         composites.append(factors[factors.index(factor)])
# print(factors)
# print(composites)
# result = list(set(factors) - set(composites))
# print(result)
# print(max(result))
