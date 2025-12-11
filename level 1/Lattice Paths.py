from math import comb

x = 20
y = 20

total_moves = x + y

answer = comb(total_moves, x)
print(answer)