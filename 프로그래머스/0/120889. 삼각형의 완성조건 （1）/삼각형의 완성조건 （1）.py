def solution(sides):
    answer = 0
    maxnum = max(sides)
    for i in sides:
        answer += i
    answer -= maxnum
    
    if maxnum < answer:
        return 1
    else:
        return 2