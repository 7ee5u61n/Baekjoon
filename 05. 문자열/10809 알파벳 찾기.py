# 아스키코드 a = 97 z = 122
while True:
    S = list(map(str, input().lower())) # 소문자로만 이루어진 단어 S
    if 0 <= len(S) <= 100:
        break
    else:
        print('100자 이하의 단어를 입력하시오')

asciiList = [-1 for _ in range(26)] # -1이 26개 있는 리스트

for i in S:
    asciiList[ord(i)-97] = S.index(i) # 알파벳이 몇번째 있는지

print(*asciiList)