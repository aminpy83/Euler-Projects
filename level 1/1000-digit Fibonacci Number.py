cache = {1: 1, 2: 1}


def fib(n):
    if n in cache:
        return cache[n]
    n1 = 1
    n2 = 1
    for i in range(3, n + 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    cache[n] = n3
    return n3


num = 1
while len(str(fib(num))) != 1_000:
    print(len(str(fib(num))))
    num += 1

print(fib(num), num, sep='\n')
