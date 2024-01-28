W = input()

counter = 0

while True:
    T = input()
    if T == "END_OF_TEXT":
        break
    else:
        counter += T.lower().split().count(W)

print(counter)