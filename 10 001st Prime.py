def is_prime(n):
    i = 2
    # if n == 2:
    #     return n
    # else:
    while i**2 <= n:
            if n % i == 0:
                return False
            i += 1
    return n

count = 6
num = 15
prime = 0
while count != 10001 :
    if is_prime(num):
        count += 1
        prime = is_prime(num)
        # print(count, prime)
    num += 2
print(prime)
