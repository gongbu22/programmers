def solution(n):
    answer = 0
    for i in range(n, 0, -2):
        if n % 2 == 0:
            answer += i*i
        else:
            answer += i
    return answer