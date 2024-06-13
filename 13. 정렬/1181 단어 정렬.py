N = int(input())
words = []
for _ in range(N):
    word = str(input())
    if word not in words: # 중복 없을 시 리스트에 삽입
        words.append(word)
words.sort(key= lambda x:(len(x), x)) # 글자수, 사전순으로 정렬

for i in range(len(words)):
    print("".join(words[i]))