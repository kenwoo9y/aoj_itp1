n = int(input())
x = 0

for i in range(1, n+1):
    if i % 3 == 0:
        print(i, end=' ')
    else:
        x = i
        while x > 0:
            if x % 10 == 3:
                print(i, end=' ')
                break
            x //= 10