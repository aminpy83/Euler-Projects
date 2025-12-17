# week = {'sun': 1, 'mon': 2, 'tue': 3, 'wed': 4, 'tur': 5, 'fri': 6, 'sat': 7}
months = ['ja31', 'fe28', 'ma31', 'ap30', 'my31', 'jn30', 'ju31', 'au31', 'se30', 'oc31', 'no30', 'de31']
its_sunday = 7  # 1/7/1901      # first sunday of month
count = 0

# 1 Jan 1900 was a Monday.
# and first sunday is 7th jan so I have first sunday move (for line 18)

for i in range(1, 101):                  # years
    if i % 4 == 0:
        months[1] = 'fe29'
    else:
        months[1] = 'fe28'

    for j in months:                     # months
        try:
            next_month = months[months.index(j) + 1]
            delta = int(next_month[2:]) - 28          # first sunday move after  next month (next j) /// % 7
        except IndexError:
            delta = 3                                 # delta in january
        its_sunday += delta
        if its_sunday > 7:
            its_sunday -= 7
        if its_sunday == 1:
            count += 1
            print(j, i, count)
print(count)
