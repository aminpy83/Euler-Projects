n = 100
fact = 1

for i in range(1, n + 1):
    fact *= i

fact = str(fact)
x = fact[1:-1].replace('', '+')
fact = fact.replace(fact[1:-1], x)
print(eval(fact))
