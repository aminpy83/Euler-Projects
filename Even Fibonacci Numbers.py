def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return fib(n-1) + fib(n-2)
    return 0

i = 1
count = 0

while fib(i) <= 4000000:
    if fib(i) % 2 == 0:
        count += fib(i)
        # print('i=',i,'------', fib(i))
    i += 1
print(count)