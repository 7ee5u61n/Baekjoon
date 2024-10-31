import sys
input = sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0
for i, j in meeting:
    if i >= end:
        count += 1
        end = j

print(count)