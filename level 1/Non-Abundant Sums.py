# a + b = c
# a , b are abundant
#smallestabundant is 12

abundant_cache = set()
def is_abundant(n):
    if n in abundant_cache:
        return True
    divs_sum = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divs_sum += i
    if n <= divs_sum:
        abundant_cache.add(n)
        return True
    return False

def c_finder(num):      # return c if it couldn't find the two abundant
    for i in range(12, num // 2 + 1):
        if i in abundant_cache and  (num - i) in abundant_cache:
            return False
        elif is_abundant(i) and  is_abundant(num - i):
            return False
    return num


last = 28123
total_sum = sum(range(13))
for x in range(13, last+1):
    if c_finder(x):
        total_sum += x
        print(x)
print(total_sum)