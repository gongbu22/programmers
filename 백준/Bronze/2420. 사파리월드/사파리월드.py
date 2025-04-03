a, b = map(float, input().split())
if ((a<0 and b>0) or (a>0 and b<0)):
    print(int(abs(a)+abs(b)))
else:
    print(int(abs(a-b)))