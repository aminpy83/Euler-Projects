sort_count = 1
nums = list(range(10))
# while sort_count < 1_000_000:
for num in nums:
    changing_nums = set(nums) - {num}
    consts = str(num)
    for j in changing_nums:
        a = consts + str(j) + str(sorted(changing_nums - {j}))
        print(a)


    break