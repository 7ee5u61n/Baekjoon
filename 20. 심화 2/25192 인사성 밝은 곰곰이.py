import sys

N = int(input())

count = 0
oldFace = set

for i in range(N):
    chat = sys.stdin.readline().rstrip()
    
    if chat == 'ENTER':
        oldFace = set() # ENTER일 경우 초기화
    
    elif chat not in oldFace:
        oldFace.add(chat)
        count += 1

print(count)