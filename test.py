def analyze(S):
    # 아스키코드 공백: 32, 숫자: 48~57, 대문자: 65~90, 소문자: 97~122
    space = 0
    number = 0
    upper = 0
    lower = 0

    for i in range(len(S)):
        if ord(S[i]) == 32:
            space += 1
        elif 48 <= ord(S[i]) <= 57:
            number += 1
        elif 65 <= ord(S[i]) <= 90:
            upper += 1
        elif 97 <= ord(S[i]) <= 122:
            lower += 1

    return lower, upper, number, space
    
while True:
    try:
        S = str(input())
        print(*analyze(S))
    except EOFError:
        break