week = {'sun': 1, 'mon': 2, 'tue' : 3, 'wed': 4, 'tur': 5, 'fri': 6, 'sat': 7}
months = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30,
          'jul': 31, 'aug': 31, 'sep': 30, 'oct': 31, 'nov': 30, 'dec': 31}
count = 0
its_sunday = 0

# 1 Jan 1900 was a Monday.
# so first sunday is 7th jan

for i in range(1, 101):                         #years
    if i % 4 == 0:
        months['feb'].value = 29
    else :
        months['feb'].value = 28
    for j in months.values():                   #months
        for k in range(1, j+1, 7):              #days


            if k + 7 >  j: