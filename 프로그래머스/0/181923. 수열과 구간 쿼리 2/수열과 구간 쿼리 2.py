def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        n = []
        for i in range(s, e+1):
            if arr[i] > k:
                n.append(arr[i])
        if n:
            answer.append(min(n))
        else:
            answer.append(-1)
                  
    return answer