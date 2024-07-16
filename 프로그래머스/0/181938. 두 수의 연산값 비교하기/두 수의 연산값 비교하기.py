def solution(a, b):
    mul = 2 * a * b
    a, b = str(a), str(b)
    answer = int(a + b)
    
    if answer < mul:
        return mul
    else:
        return answer