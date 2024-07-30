def solution(my_string):
    answer = []
    print(ord('r')-65)
    for i in range(52):
        answer.append(0)
    for s in my_string:
        if ord(s) < 91:
            answer[ord(s)-65] += 1
        else:
            answer[ord(s)-71] += 1
    return answer