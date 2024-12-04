n = int(input())
word = str(input())

while True:
    if 'PS4' in word or 'PS5' in word:
        word = word.replace('PS4', 'PS').replace('PS5', 'PS')
    else:
        break

print(word)