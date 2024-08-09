def solution(num_list):
    odd = num_list[::2]
    even = num_list[1::2]
    if sum(odd) < sum(even):
        return sum(even)
    else:
        return sum(odd)
        