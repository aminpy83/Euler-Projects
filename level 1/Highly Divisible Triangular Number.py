from math import floor
factors = 1
x = 1

while True:
    y = x * (x+1) // 2          #sum(range(x+1))
    for i in range(1, (y// 2) +1 ):
        if y % i == 0:
            factors += 1
    if factors > 500:
        print(x, y, factors)
        break
    print(y, factors)
    factors = 1
    x += 1