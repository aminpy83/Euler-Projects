a = str(2 ** 1000)
# print(a)
b = a[1:-1]
# print(b)
b = b.replace('', '+')
a = a.replace(a[1: -1], b)
print(eval(a))
