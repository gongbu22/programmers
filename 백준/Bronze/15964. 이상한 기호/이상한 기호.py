def a(a, b):
    return (a+b)*(a-b)

first, second = map(int, input().split())

print(a(first, second))