while True:
    H,W = map(int, input().split())
    if H == 0 and W == 0:
        break

    for i in range(H):
        for j in range(W):
            if i % 2 == 0:
                if j % 2 == 0:
                    print("#", end='')
                else:
                    print(".", end='')
            else:
                if j % 2 == 0:
                    print(".", end='')
                else:
                    print("#", end='')
        print("")
    print()