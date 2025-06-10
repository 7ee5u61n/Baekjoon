n = int(input())

# 약속 기록
record = [list(input().split()) for _ in range(n)]
# 0: 약속 없음
plan = [0]*70

for i in range(n):
    name, m = input().split()
    for s, w, d, p in record:
        if name == s:
            if int(m) >= int(p):
                day = (int(w)-1)*7+int(d)
                plan[day] += 1
                break
            break
    
result = 0
value = 0
for i in range(70):
    if plan[i] == 0:
        value = 0
    else:
        value += 1
    result = max(value, result)

print(result)