# a = range(0,1001)
# adder = 0
# for i in a:
#     if i % 3 == 0 or i % 5 == 0:
#         adder += i
# print(adder)

#--------------------------------------------------

a = sum(range(3,1000,3)) + sum(range(5, 1001, 5)) - sum(range(15, 1001, 15))
print(a)