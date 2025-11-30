from math import sqrt

# Among the first 384 thousand square numbers, what is the sum of all the odd squares?
sum_of_odds = 0
for i in range (1, 384_000, 2):
    sum_of_odds += i ** 2
print(sum_of_odds)