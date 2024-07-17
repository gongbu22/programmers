def solution(num_list):
    onum = ''
    dnum = ''
    for i in num_list:
        if (i % 2 == 0):
            dnum += str(i)
        else:
            onum += str(i)
            
    return int(onum) + int(dnum)