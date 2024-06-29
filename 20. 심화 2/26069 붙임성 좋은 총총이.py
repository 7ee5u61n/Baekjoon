import sys

N = int(input())

rainbowDancer = set()

for i in range(N):
    meet = list(map(str, sys.stdin.readline().split()))
    if meet[0] == 'ChongChong' or meet[1] == 'ChongChong':
        rainbowDancer.update(meet)
    elif meet[0] in rainbowDancer or meet[1] in rainbowDancer:
        rainbowDancer.update(meet)

print(len(rainbowDancer))