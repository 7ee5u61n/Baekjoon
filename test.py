import sys
input = sys.stdin.readline

n = int(input())

card = {}
for _ in range(n):
    number = int(input())
    if number in card:
        card[number] += 1
    else:
        card[number] = 1

result = sorted(card.items(), key=lambda x:(-x[1],x[0]))
print(result[0][0])