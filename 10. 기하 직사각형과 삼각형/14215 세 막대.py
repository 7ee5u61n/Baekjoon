a, b, c = map(int, input().split())
length = [a, b, c]

i = 0
while True: # 삼각형 만들 때 까지 긴변의 길이 1 빼기
    value = max(length) - i
    if value < a + b + c - max(length):
        length.append(value)
        break
    i += 1
length.remove(max(length))

print(sum(length))