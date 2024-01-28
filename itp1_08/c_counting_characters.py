texts = ""
while True:
    try:
        texts += input().lower()
    except EOFError:
        break

counter = [0] * 26

letters = "abcdefghijklmnopqrstuvwxyz"
for text in texts:
    i = 0
    for letter in letters:
        if text == letter:
            counter[i] += 1
        i += 1

for i in range(26):
    print(letters[i] + " : " + str(counter[i]))