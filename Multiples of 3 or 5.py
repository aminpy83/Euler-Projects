# a = range(0,1000)
# adder = 0
# for i in a:
#     if i % 3 == 0 or i % 5 == 0:
#         adder += i
# print(adder)

#--------------------------------------------------

a = sum(range(3,1000,3)) + sum(range(5, 1000, 5)) - sum(range(15, 1000, 15))
print(a)