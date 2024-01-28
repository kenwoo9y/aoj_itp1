n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

for p in range(1,4):
    D = sum(abs(x - y)**p for x,y in zip(X,Y))**(1/p)
    print(f"{D:.6f}")

D_infinity = max(abs(x - y) for x,y in zip(X,Y))
print(f"{D_infinity:.6f}")