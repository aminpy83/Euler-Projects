max_num = 0
for i in range(999,100,-1):
    for j in range(999, 100, -1):
        if  j*i < max_num :
            break
        if str(i * j)[::] == str(i * j)[-1::-1] :
            max_num = i * j
            print(i, j, max_num)
