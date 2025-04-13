word = input()

for _ in range(len(word) // 10 + 1):
    print(word[:10])
    word = word[10:]