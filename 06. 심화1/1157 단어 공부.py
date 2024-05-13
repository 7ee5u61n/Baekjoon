# 아스키 A = 65 Z = 90
S = list(str(input().upper())) # 대소문자로 이루어진 알파벳

frequency = [0]*26

for i in range(len(S)): # 알파벳 빈도수 리스트에 저장
    frequency[ord(S[i])-65] = frequency[ord(S[i])-65] + 1

sortedFrequency = sorted(frequency, reverse=True)

if sortedFrequency[0] == sortedFrequency[1]: # 제일 큰 값이 여러개인지 확인
    print('?') # 여러개라면 ? 출력
else:
    print(chr(frequency.index(max(frequency))+65))  # 아니면 제일 많이 사용된 알파벳 출력
