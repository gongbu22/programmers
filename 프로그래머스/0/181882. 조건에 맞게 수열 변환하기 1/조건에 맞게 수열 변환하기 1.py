def solution(arr):
    for idx, num in enumerate(arr):
        if (num % 2 == 0) and (num >= 50):
            arr[idx] = num / 2
        elif (num % 2 == 1) and (num <= 50):
            arr[idx] = num * 2
    return arr