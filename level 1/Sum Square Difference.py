square_of_sums = sum(range(1, 101)) ** 2
sum_of_squares = sum (i*i for i in range(1, 101))
print(abs(square_of_sums - sum_of_squares))

# for i in range(1, 101):
#     sum_of_squares += (i ** 2)
