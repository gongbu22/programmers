def solution(my_string, s, e):
    mstring=my_string[s:e+1]
    restr=mstring[::-1]
    return my_string[:s] + restr + my_string[e+1:]