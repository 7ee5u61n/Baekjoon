time = [(600, 600), (1320, 1320)]
n = int(input())
for i in range(n):
    start, end = map(str, input().split())
    start = (int(start[0:2])*60+int(start[2])*10+int(start[3])-10)
    end = (int(end[0:2])*60+int(end[2])*10+int(end[3])+10)
    time.append((start, end))

time.sort()

rest_time = 0
last_time = 600

# 놀이기구 중간 쉬는 시간
for start, end in time:
    rest_time = max(rest_time, start - last_time)
    last_time = max(last_time, end)
    
print(rest_time)