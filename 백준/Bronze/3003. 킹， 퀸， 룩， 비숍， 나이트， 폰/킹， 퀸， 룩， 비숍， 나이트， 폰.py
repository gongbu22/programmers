nums = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
result = [0]*6


for i in range(0, len(nums)):
    result[i] = str(chess[i] - nums[i])

print(' '.join(result))