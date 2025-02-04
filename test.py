n = int(input())
winner = 1
mx_score = 0
for people in range(1, n+1):
    card = list(map(int, input().split()))
    score = 0

    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                digit = (card[i]+card[j]+card[k])%10
                if digit >= score:
                    score = digit
    
    if score >= mx_score:
        mx_score = score
        winner = people

print(winner)