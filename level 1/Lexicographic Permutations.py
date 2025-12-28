from itertools import permutations

numbers = list(range(10))
nums = list(map(lambda x: str(x), numbers))

a = list(permutations(nums))
print(a[999_999])
