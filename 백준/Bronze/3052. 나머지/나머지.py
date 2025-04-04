arr = []

for _ in range(10):
    a = int(input())

    arr.append(a % 42)

result = []

for i in arr:
    if i not in result:
        result.append(i)

print(len(result))