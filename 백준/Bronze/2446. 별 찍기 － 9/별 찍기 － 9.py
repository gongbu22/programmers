n = int(input())

for i in range(n):
    star = 2*(n-i)-1
    empty = i

    print(' '*empty + '*'*star)

for i in range(2, n+1):
    print(' '*(n-i) + '*'*(2*i-1))