def amicable(num):
    divs = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divs.append(i)

    pair_num = sum(divs)
    divs = []
    for j in range(1, pair_num // 2 + 1):
        if pair_num % j == 0:
            divs.append(j)

    if sum(divs) == num and num != pair_num:
        return num, pair_num
    return False


amicable_nums = []
for number in range(10_000):
    if number in amicable_nums:
        continue
    try:
        x, y = amicable(number)
        amicable_nums.append(x)
        amicable_nums.append(y)
    except:
        continue
print(amicable_nums, sum(amicable_nums), sep='\n')
