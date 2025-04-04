t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    result = ''

    last = (n - 1) // h + 1
    
    if (n % h == 0):
        front = h
    else:
        front = n % h

    if len(str(last)) != 2:
        last = "0" + str(last)
    
    result = str(front) + str(last)
    print(result)
    
