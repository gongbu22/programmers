n = int(input())

for _ in range(n):
    ox = input()

    score = 0
    result = 0

    for i in ox:

        if i == "O":
            score += 1
            result += score
        else:
            score = 0
    
    print(result)