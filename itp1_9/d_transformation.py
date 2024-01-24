str = input()
q = int(input())

for _ in range(q):
    inputs = list(input().split())
    order = inputs[0]
    a = int(inputs[1])
    b = int(inputs[2])

    if order == "print":
        print(str[a:b+1])
    elif order == "reverse":
        reverse_target = str[a:b+1]
        str = str[:a] + reverse_target[::-1] + str[b+1:]
    elif order == "replace":
        p = inputs[3]
        str = str[:a] + p + str[b+1:]
    else:
        pass