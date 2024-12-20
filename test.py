cu, du = map(int, input().split())
cd, dd = map(int, input().split())
cp, dp = map(int, input().split())
h = int(input())

time = 0
while True:
    if time == 0:
        h -= (du+dd+dp)
    else:
        if time%cu == 0:
            h -= du
        if time%cd == 0:
            h -= dd
        if time%cp == 0:
            h -= dp
    if h <= 0:
        break
    else:
        time += 1
        
print(time)