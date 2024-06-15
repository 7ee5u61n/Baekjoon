import sys
N, M = map(int, sys.stdin.readline().split())

unheard = set()
for _ in range(N):
    name = sys.stdin.readline().rstrip() # 듣도 못한 사람
    unheard.add(name)

unseen = set()
for _ in range(M):
    name = sys.stdin.readline().rstrip() # 보도 못한 사람
    unseen.add(name)

unheard_unseen = list(unheard & unseen) # 듣도 보도 못한 사람
unheard_unseen.sort()

print(len(unheard_unseen))
for i in range(len(unheard_unseen)):
    print(unheard_unseen[i])