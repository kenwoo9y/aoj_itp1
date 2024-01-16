r,c = map(int, input().split())
sheet = [list(map(int, input().split())) for i in range(r)]

for i in range(r):
    sheet[i].append(sum(sheet[i]))

column_sum = [0] * (c+1)
for j in range(c+1):
    for k in range(r):
        column_sum[j] += sheet[k][j]

for i in range(r):
    print(*sheet[i])
print(*column_sum)