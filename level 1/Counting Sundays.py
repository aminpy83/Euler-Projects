# week = {'sun': 1, 'mon': 2, 'tue': 3, 'wed': 4, 'tur': 5, 'fri': 6, 'sat': 7}
months = ['ja31', 'fe28', 'ma31', 'ap30', 'my31', 'jn30', 'ju31', 'au31', 'se30', 'oc31', 'no30', 'de31']
its_sunday = 0  # 1/0/1901
count = 0

# 1 Jan 1900 was a Monday.
# so first sunday is 7th jan

for i in range(1, 101):         # years
    if i % 4 == 0:
        months[1] = 'fe29'
    else:
        months[1] = 'fe28'
    for j in months:            # months
        delta = abs(int(j[2:]) - 28)          # move
        its_sunday += delta

        last_month =  int(j[2:])
        if its_sunday > last_month:
            its_sunday -= last_month

        if its_sunday == 1:
            count += 1
print(count)
