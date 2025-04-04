word = input()
result = [-1]*26

for i in range(len(word)):
    if result[ord(word[i])-97] == -1:
        result[ord(word[i])-97] = i

print(' '.join(map(str, result)))