from math import sqrt

P = list(map(float, input().split()))

d = sqrt((P[0] - P[2]) ** 2 + (P[1] - P[3]) ** 2)
print(f"{d:.8f}")