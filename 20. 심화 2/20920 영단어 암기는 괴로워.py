import sys

N, M = map(int, sys.stdin.readline().split())

words = {}
for i in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

arr = [(words[i], len(i), i) for i in words] # 빈도수, 글자 수, 단어 저장 배열
arr.sort(key=lambda x:(-x[0], -x[1], x[2])) # 빈도수, 글자 수, 알파벳 순 정렬

for i in arr:
    print(i[2])