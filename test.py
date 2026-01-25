a, b, c = map(int, input().split())

n = int(input())
result = 0
for _ in range(n):
    teamPoint = 0
    for _ in range(3):
        x, y, z = map(int, input().split())
        teamPoint += x * a + y * b + z * c
    result = max(result, teamPoint)

print(result)