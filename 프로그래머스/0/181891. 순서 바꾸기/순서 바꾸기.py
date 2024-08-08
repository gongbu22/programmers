def solution(num_list, n):
    first_num = num_list[n:]
    last_num = num_list[:n]
    return first_num+last_num