def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        j, k  = parts[i]
        answer += my_strings[i][j:k+1]
    return answer