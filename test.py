T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    for _ in range(h):
        meat = input()
        print(meat[::-1])