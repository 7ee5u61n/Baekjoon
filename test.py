C = int(input())

max = 0
for _ in range(C):
    code = str(input())
    
    repeat = 0
    for i in range(len(code)):
        if 'for' in code[i:i+3]:
            repeat += 1
        elif 'while' in code[i:i+5]:
            repeat += 1

    if max < repeat:
        max = repeat

print(max)