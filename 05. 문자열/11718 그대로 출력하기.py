while True:
    try:
        word = input()
        print(word)
        if len(word) == '':
            break
    except EOFError:
        break