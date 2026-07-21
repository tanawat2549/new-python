score = int(input("Enter the score: "))
while score < 0 or score > 100:
    print('ERROR:cannot be negative')
    print('or grearer than 100.')
    score = int(input('Enter the correct score: '))
