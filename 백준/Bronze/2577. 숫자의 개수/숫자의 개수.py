a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
arr = [0]*10

for i in result:
    arr[int(i)] += 1

for j in arr:
    print(j)