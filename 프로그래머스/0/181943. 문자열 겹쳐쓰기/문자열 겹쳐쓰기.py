def solution(my_string, overwrite_string, s):
    answer = ''
    answer1 =my_string[:s]
    answer2 =overwrite_string
    answer3 =my_string[s+len(overwrite_string):]
    
    return answer1 + answer2 + answer3