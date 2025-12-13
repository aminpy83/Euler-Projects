from pprint import pprint
triangle = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
# nums, ls = [], []
# a = enumerate(triangle)
# i = 0
#making triangle
# while i < len(triangle) -2:
#     if triangle[i] == '\n' or triangle[i] == ' ':
#         pass
#
#     elif (triangle[i].isnumeric() and triangle[i+1]).isnumeric():
#         num = triangle[i]+triangle[i+1].]
#         ls.append(int(num))
#
#         if '\n' in triangle[i+2]:
#             nums.append(ls)
#             ls = []
#     i += 1
# pprint(nums)

# def max_finder(l):
#     lst = ls.copy()
#     first_max = lst.index(max(lst))
#     max(lst.pop(first_max))

# triangle
triangle = triangle[1:].splitlines()
nums = []
for line in triangle:
    line = line.split(' ')
    x = map(int, line)
    nums.append(list(x))
pprint(nums)

