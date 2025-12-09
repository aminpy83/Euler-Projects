counter = 0
max_chain = [0, 0]
def collatz(n):
    global counter
    counter += 1
    if n % 2 == 0:
        n //= 2
        return collatz(n)
    elif n == 1:
        return 1, counter
    else:
        n = 3 * n + 1
        return collatz(n)


x = 13
while x < 1_000_000:
    collatz(x)
    if counter > max_chain[0]:
        max_chain = counter, x
    counter = 0
    x += 1
    print(x)
print(max_chain)
