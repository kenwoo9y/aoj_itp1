houses = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]

n = int(input())
for i in range(n):
    b,f,r,v = map(int, input().split())
    houses[b-1][f-1][r-1] += v

for b in range(4):
    for f in houses[b]:
        print("", *f)
    if b != 3:
        print("#" * 20)