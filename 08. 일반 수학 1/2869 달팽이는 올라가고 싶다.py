import math
A, B, V = map(int, input().split()) # A올라가고 B미끄러짐 V높이 막대

count = 0 # 며칠
height = 0 # 오늘 높이

if A >= V:
    count = 1
elif A - B == 1:
    count = V - B
else:
    count = math.ceil((V-B)/(A-B))

print(count)