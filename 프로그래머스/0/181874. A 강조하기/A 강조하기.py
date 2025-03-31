def solution(myString):
    answer = ''
    for i in myString:
        if i == "a":
            answer += i.upper()
        elif (ord(i) > 65 or ord(i) < 97) and i != "A":
            answer += i.lower()
        else:
            answer += i
    return answer