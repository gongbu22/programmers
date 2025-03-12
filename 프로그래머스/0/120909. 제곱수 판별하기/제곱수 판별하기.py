def solution(n):
    answer = 0
    m = int(n ** 0.5)
    if m ** 2 == n:
        answer = 1
    else:
        answer = 2
    return answer