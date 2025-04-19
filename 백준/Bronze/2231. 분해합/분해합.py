n = int(input())

start = max(1, n - 9*len(str(n)))

result = 0

for m in range(start, n):
    decomposition = m + sum(map(int, str(m)))
    if decomposition == n:
        result = m
        break

print(result)