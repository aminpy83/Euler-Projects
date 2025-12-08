# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2:
#         return fib(n-1) + fib(n-2)
#     return 0

# l = {}
# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2:
#         if n in l:
#             return l[n]
#         l[n] = fib(n-1) + fib(n-2)
#         return l[n]
#     return 0

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    n1 = 1
    n2 = 2
    for _ in range(3, n + 1):
        n = n1 + n2
        n1 = n2
        n2 = n
    return n

i = 1
count = 0

while fib(i) <= 4000000:
    if fib(i) % 2 == 0:
        count += fib(i)
        # print('i=',i,'------', fib(i),i)
    i += 1
print(count)
