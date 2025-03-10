def solution(n):
    answer = 0
    arr = [ i for i in str(n)]
    for j in arr:
        answer += int(j)
    return answer