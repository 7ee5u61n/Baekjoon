n = int(input())
candidate = []
for _ in range(n):
    name = str(input())
    if len(name) == 3:
        candidate.append(name)

candidate.sort()
print(candidate[0])