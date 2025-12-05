from math import ceil, sqrt

factors = 1
x = 1
# y = 0

def is_prime(n):
    for j in range(2, ceil(sqrt(n))):
        if n % j == 0:
            return False
    return True

while True:
    y = x * (x + 1) // 2               #y += x           #sum(range(x+1))
    if is_prime(y):
        x += 1
        continue
    else:
        for i in range(1, ceil(sqrt(y)) ):
            if y % i == 0:
                factors += 2
        if factors > 500:
            print(x, y, factors)
            break
        print(y, factors)
        factors = 1
        x += 1