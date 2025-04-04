arr = []
maxnum = 0

while(True):
    try:
        a = int(input())
        arr.append(a)
    except EOFError:
        break

print(max(arr))
print(arr.index(max(arr))+1)