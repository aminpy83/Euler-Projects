def IsPrime(n):
    for i in range(2, n// 2+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
factors = []
fact = num
prime = 3
while prime <= num // 2 + 1 :
    if fact % 2 == 0:
        factors.append(2)
    elif fact % prime == 0:
        factors.append(prime)
    prime += 2
print(factors)
for factor in factors:
    if not(IsPrime(factor)):
        factors.pop(factors.index(factor))
print(factors)