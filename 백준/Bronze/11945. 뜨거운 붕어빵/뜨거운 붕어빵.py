a, b = map(int, input().split())

for _ in range(a):
    bread = input()

    print(''.join(reversed(bread)))