n, s = map(str, input().split())

# 채팅 기록
arr = []
# 정답
answer = ''
for i in range(int(n)):
    name, chat = map(str, input().split())
    arr.append([name, chat])
    if name == s:
        answer = chat

# 당첨자 이전에 정답인 사람
count = 0
for name, chat in arr:
    if chat == answer:
        # 당첨자
        if name == s:
            break
        count += 1
        
print(count)