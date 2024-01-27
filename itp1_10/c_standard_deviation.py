from math import sqrt

while True:
    n = int(input())

    if n == 0:
        break

    s = list(map(int, input().split()))

    m = sum(s) / n

    total_deviation = 0
    for i in range(n):
        total_deviation += (s[i] - m)**2
    
    standard_deviation = sqrt(total_deviation / n)

    print(standard_deviation)
