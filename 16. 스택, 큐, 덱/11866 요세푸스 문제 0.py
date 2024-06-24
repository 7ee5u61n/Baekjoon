from collections import deque

N, K = map(int, input().split())

people = deque(range(1, N+1))

joshephus = []
for _ in range(N):
    for _ in range(K-1):
        people.append(people.popleft())
    joshephus.append(people.popleft())

print('<', end='')
for i in range(len(joshephus)):
    print(str(joshephus[i]), end="")
    if joshephus[i] != joshephus[-1]:
        print(',', end=" ")
print('>', end="")