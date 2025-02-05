n, m = map(int, input().split())

total = int(1440*(m/n))

hour = str(total//60)
minutes = str(total%60)

if len(hour) == 1:
    hour = '0'+hour
if len(minutes) == 1:
    minutes = '0'+minutes

print(f'{hour}:{minutes}')