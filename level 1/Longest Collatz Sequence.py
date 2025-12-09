# def collatz(n):
#     global counter
#     counter += 1
#     if n % 2 == 0:
#         n //= 2
#         return collatz(n)
#     elif n == 1:
#         return 1, counter
#     else:
#         n = 3 * n + 1
#         return collatz(n)

max_chain = [0, 0]
x = 13
dic = {1: 1}

while x < 1_000_000:
    counter = 0
    n = x

    while n not in dic:
        counter += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    counter += dic[n]
    dic[x] = counter
    if counter > max_chain[0]:
        max_chain[0], max_chain[1] = counter, x
    x += 1
    print(x)
print(max_chain)
