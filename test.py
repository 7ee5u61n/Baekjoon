result = ''
for _ in range(15):
    pixel = list(input().split())
    for i in range(15):
        if pixel[i] == 'w':
            result = 'chunbae'
        elif pixel[i] == 'b':
            result = 'nabi'
        elif pixel[i] == 'g':
            result = 'yeongcheol'

print(result)