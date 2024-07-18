def solution(numLog):
    wsda = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    result = ''
    for i in range(len(numLog)):
        for key, value in wsda.items():
            if (i != 0) & (numLog[i] - numLog[i-1] == value):
                result += key
    return result