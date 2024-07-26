def solution(my_string, m, c):
    first=[]
    result =''
    for i in range(0, len(my_string), m):
        first.append(my_string[i:i+m])
    for j in first:
        result += j[c-1:c]
    return result