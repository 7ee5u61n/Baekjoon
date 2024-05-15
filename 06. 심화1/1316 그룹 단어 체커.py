# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어에서 문자의 연속이 끝나면 금지 리스트에 집어 넣고 금지 리스트에 있는 문자가 다시 나오면 그룹 단어가 아니게 만들기

N = int(input()) # 단어의 개수

nonGroupWord = 0

for _ in range(N):
    word = (str(input()))
    banLetter = [] # 반복이 끝나 더이상 나오면 안되는 단어
    for i in range(len(word)):
        i += 0
        banLetter.append(word[i]) # 앞으로 나오지 말아야 할 문자 저장하는 리스트

print(len(word))
print(banLetter)