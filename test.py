result = 0
while True:
    try:
        s = str(input())
        result += 1
    except EOFError:
        break

print(result)