n,m,l = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    C = []
    for j in range(l):
        sum = 0
        for k in range(m):
            sum += A[i][k] * B[k][j]
        C.append(sum)
    print(*C)