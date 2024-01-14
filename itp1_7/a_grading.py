grade = ''

while True:
    m,f,r = map(int, input().split())

    if m < 0 and f < 0 and r < 0:
        break

    if m < 0 or f < 0:
        grade = 'F'
    elif m + f >= 80:
        grade = 'A'
    elif 65 <= m + f < 80:
        grade = 'B'
    elif 50 <= m + f < 65:
        grade = 'C'
    elif 30 <= m + f < 50:
        if r >= 50:
            grade = 'C'
        else:
            grade = 'D'
    else:
        grade = 'F'
        
    print(grade)