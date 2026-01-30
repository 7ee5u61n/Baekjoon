jinho = str(input())
n = int(input())
result = 0
for _ in range(n):
    mbti = str(input())
    if mbti == jinho:
        result += 1

print(result)