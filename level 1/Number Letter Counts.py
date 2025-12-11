one_digs = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
two_digs1 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
             'seventeen', 'eighteen', 'nineteen']
two_digs2 = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
three_digs = ['', 'onehundred', 'twohundred', 'threehundred', 'fourhundred', 'fivehundred',
              'sixhundred', 'sevenhundred', 'eighthundred', 'ninehundred']
four_digs = 'onethousand'

# print(list(map(lambda x: x + 'hundred', one_digs)))
used_letters = 0

# (10, 19, 100)
# for i in three_digs:
# for j in two_digs1:
#     if i == '':
#         used_letters += len(i) + len(j)
#     else:
#         used_letters += len(i) + len(j) + 3

for i in three_digs:
    for j in two_digs2:
        for k in one_digs:

            if (k == '' and j == '') or (i == ''):
                used_letters += len(i) + len(j) + len(k)
            else:
                used_letters += len(i) + len(j) + len(k) + 3

    for l in two_digs1:
        if i == '':
            used_letters += len(i) + len(l)
        else:
            used_letters += len(i) + len(l) + 3

print(used_letters + len(four_digs))
