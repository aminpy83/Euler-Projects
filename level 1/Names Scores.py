with open('/home/amin/Downloads/0022_names.txt', 'r') as f:
    content = f.read()
    content = content.replace(r'"', '')
    ls = sorted(content.split(','))

print(ls)
words_value = {}
for i in ls:
    val = 0
    for j in i:
        val += ord(j) - 64          # j ascii code
    words_value[i] = val

print(words_value['COLIN'])
print(ls.index('COLIN'))

total_values = 0
for name in ls:
    total_values += (ls.index(name) + 1) * words_value[name]
print(total_values)