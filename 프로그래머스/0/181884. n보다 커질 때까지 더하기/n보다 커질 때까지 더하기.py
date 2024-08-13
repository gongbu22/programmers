def solution(numbers, n):
    sum = 0
    for num in numbers:
        if sum > n:
            break
        sum += num        
    return sum