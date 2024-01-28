cards = [(s, n) for s in ['S', 'H', 'C', 'D'] for n in range(1, 14)]
given_cards = []

n = int(input())
for i in range(n):
    suit, number = input().split()
    number = int(number)
    given_cards.append((suit, number))

for card in cards:
    if card not in given_cards:
        print(*card)
