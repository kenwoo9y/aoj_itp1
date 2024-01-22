while True:
    cards = input()

    if cards == "-":
        break

    m = int(input())
    for _ in range(m):
        h = int(input())

        formar = cards[:h]
        later = cards[h:]
        
        cards = later + formar
    
    print(cards)