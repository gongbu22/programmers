def solution(a, b):
    result = int(str(a) + str(b))
    if int(str(a) + str(b)) < int(str(b) + str(a)):
        result = int(str(b) + str(a))
    
    return result