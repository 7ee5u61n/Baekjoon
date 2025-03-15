n = int(input())
compression = dict()

for _ in range(n):
    lower, upper = map(str, input().split())
    compression[upper] = lower

packed = str(input())
unpacked = ''
for i in packed:
    unpacked += compression[i]

s, e = map(int, input().split())
print(unpacked[s-1:e])