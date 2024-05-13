S = list(str(input())) # 1이상 100이하 길이의 소문자 단어

compareList = [] # 비교 결과를 저장하는 리스트

def palidrome(S): 
    for i in range(len(S)//2): # 홀수일때 가운데 문자는 상관 없음
        i += 0
        if S[i] == S[-i-1]: # 단어 앞뒤 비교하여 같으면 1 아니면 0 리스트에 삽입
            compareList.append(1)
        else:
            compareList.append(0)
    if 0 in compareList: # 리스트에 0이 있으면 0출력 아니면 (팰린드롬 이므로) 1출력
        print(0)
    else:
        print(1)

palidrome(S)