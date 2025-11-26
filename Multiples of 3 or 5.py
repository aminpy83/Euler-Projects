a = range(0,1001)
adder = 0
for i in a:
    if i % 3 == 0 or i % 5 == 0:
        adder += i
print(adder)