counter = 0
def collatz(n):
    global counter
    counter += 1
    if n % 2 == 0:
        n //= 2
        return collatz(n)
    elif n == 1:
        return 1
    else:
        n = 3 * n + 1
        return collatz(n)

x = 13
while x < 1000_000:
    collatz(x)