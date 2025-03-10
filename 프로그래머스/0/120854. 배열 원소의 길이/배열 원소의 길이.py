def solution(strlist):
    answer = []
    num = 0
    for i in strlist:
        for j in i:
            num += 1
        answer.append(num)
        num = 0
    return answer