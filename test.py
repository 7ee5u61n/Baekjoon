s, c, o, n = map(int, input().split())

sn = s+n
co = c+o*2

print(min(sn//3, co//6))