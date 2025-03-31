def solution(binomial):
    arr = binomial.split(' ')
    a = int(arr[0])
    b = int(arr[2])
    if arr[1] == "+":
        answer = a + b
    elif arr[1] == "-":
        answer = a - b
    elif arr[1] == "*":
        answer = a * b
    else:
        answer = a / b
    return answer