import sys

n = int(input())
participant = {}
for i in range(n):
    name = str(input())
    if participant.get(name):
        participant[name] += 1
    else:
        participant[name] = 1

for i in range(n-1):
    name = str(input())
    participant[name] -= 1

for i, j in participant.items():
    if j == 1:
        print(i)
        break