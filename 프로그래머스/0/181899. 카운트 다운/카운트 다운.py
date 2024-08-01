def solution(start_num, end_num):
    i = start_num
    answer = []
    while i >= end_num:
        answer.append(i)
        i -= 1
    return answer