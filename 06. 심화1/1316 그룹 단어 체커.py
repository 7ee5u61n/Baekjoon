# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.


N = int(input()) # 단어의 개수

nonGroupWord = 0 # 그룹단어가 아닌 개수

for _ in range(N):
    word = (str(input()))
    for i in range(len(word)-1):
        if word.find(word[i]) > word.find(word[i+1]): 
            # word[i]가 처음 나타나는 위치가 word[i+1] 문자가 나타는 인덱스 보다 작다면 같은 문자가 연속되지 않음을 의미하므로 그룹단어가 아니다.
            nonGroupWord += 1
            break

print(N - nonGroupWord)