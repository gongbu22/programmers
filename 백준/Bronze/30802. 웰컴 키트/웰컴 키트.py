n = int(input())
c = list(map(int, input().split()))
t, p = map(int, input().split())

result_t = 0

for i in c:
    if (i>0 and i%t != 0):
        result_t += (i//t)+1
    elif (i>0 and i%t == 0):
        result_t += (i//t)
    else:
        result_t += 0
print(result_t)
print(n//p, n%p)