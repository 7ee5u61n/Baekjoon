scores = []
for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    scores.append(score)

avg = sum(scores) // 5
print(avg)