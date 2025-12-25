a, b, c = map(int, input().split())
d = int(input())

total_seconds = a * 3600 + b * 60 + c + d
new_hour = (total_seconds // 3600) % 24
new_minute = (total_seconds % 3600) // 60
new_second = total_seconds % 60

print(new_hour, new_minute, new_second)