def check(a, b, c, d, e):
    rest = (a**2 + b**2 + c**2 + d**2 + e**2)%10
    return rest

a, b, c, d, e = map(int, input().split())

print(check(a, b, c, d, e))