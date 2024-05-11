# ABC , DEF, GHI, JKL, MNO, PQRS, TUV, WXYZ 다이얼
# 아스키 A = 65 Z = 90

word = list(input()) # 알파벳 대문자로 이루어진 2이상 15이하의 단어
total = 0 # 총 시간

for i in range(len(word)):
    if word[i] in 'ABC':
        total += 3
    elif word[i] in 'DEF':
        total += 4
    elif word[i] in 'GHI':
        total += 5
    elif word[i] in 'JKL':
        total += 6
    elif word[i] in 'MNO':
        total += 7
    elif word[i] in 'PQRS':
        total += 8
    elif word[i] in 'TUV':
        total += 9
    elif word[i] in 'WXYZ':
        total += 10
        
print(total)