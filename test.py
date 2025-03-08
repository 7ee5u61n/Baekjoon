n = int(input())
score = [0]*(n+1)

for _ in range((n*(n-1))//2):
    a,b,c,d = map(int, input().split())
    if c > d:
        score[a] += 3
    elif c == d:
        score[a] += 1
        score[b] += 1
    else:
        score[b] += 3
score.pop(0)

for i in score:
    print(sorted(score, reverse=True).index(i)+1)