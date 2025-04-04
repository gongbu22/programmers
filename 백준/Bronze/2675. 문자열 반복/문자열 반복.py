n = int(input())

for _ in range(n):
    s, words = map(str, input().split())
    result = ''
    for i in words:
        result += i*int(s)

    print(result)