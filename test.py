n = int(input())
arr = list(map(int, input().split()))

connected = 0
battery = 0
previous_battery = 2
for i in range(n):
    # 이미 연결되어 있는 핸드폰에 연결
    if connected == arr[i]:
        # 직전 배터리 소모량의 2배
        previous_battery *= 2
        battery += previous_battery
    # 새로운 핸드폰 연결
    else:
        connected = arr[i]
        battery += 2
        previous_battery = 2
    if battery >= 100:
        connected = 0
        battery = 0
print(battery)