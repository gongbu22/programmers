n = int(input())

for i in range(n):
    name = input()
    result = ''
    for j in name:
        if j == 'Z':
            result += 'A'
        else:
            result += chr(ord(j)+1)

    print(f'String #{i+1}')
    print(result)
    print()