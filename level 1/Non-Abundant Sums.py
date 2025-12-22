# a + b = c
# a , b are abundant
#smallestabundant is 12

# divs_sum = last * [0]

# for i in range(1, last):
#     j = i * 2
#     for j in range(1, last // 2 +1):
#         j += i
#         divs_sum[j] += j
from math import sqrt, ceil

last = 28123


abundant_cache = set()
def is_abundant(n):
    if n in abundant_cache:
        return True

    divs_sum = set()
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            divs_sum.add(i)
            divs_sum.add(n // i)

    if n < sum(divs_sum):
        abundant_cache.add(n)
        return True
    return False


def c_finder(num):      # return c if it couldn't find the two abundant
    for i in range(12, num // 2 + 1):
        if is_abundant(i) and  is_abundant(num - i):
            return False
    return num


total_sum = sum(range(13))
for x in range(13, last+1):
    if c_finder(x):
        total_sum += x
        print(x)
print(total_sum)