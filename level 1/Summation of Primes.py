from math import sqrt
num = 2_000_000

def is_prime(n):
    if n % 2 == 0:
        if n == 2:
            return 1
        else:
            return 0
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return 0
    return 1


summation = 0
for n in range(2, num):
    if is_prime(n):
        summation += n
        print(summation)

