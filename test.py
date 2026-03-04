vowel = {'a', 'e', 'i', 'o', 'u'}
while True:
    word = str(input()).lower()
    if word == '#':
        break
    count = 0
    for w in word:
        if w in vowel:
            count += 1
    print(count)