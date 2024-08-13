def solution(arr, queries):
    for idx, a in enumerate(arr):
        for s, e in queries:
            if (s <= idx) and (idx <= e):
                arr[idx] += 1
    return arr