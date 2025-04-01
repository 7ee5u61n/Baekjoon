n, i = map(int, input().split())

handle = list(input().split() for _ in range(n))
handle.sort()

print(*handle[i-1])