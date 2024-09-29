# time = [hour, minute, second]
def timetobin(time):
    bintime = ""
    for i in range(3):
        for _ in range(6):
            bintime = str(time[i] % 2) + bintime
            time[i] //= 2
    horizontally = bintime
    vertically = ""
    for i in range(6):
        vertically += bintime[i] + bintime[i+6] + bintime[i+12]
    return (vertically, horizontally)

N = int(input())
for i in range(N):
    time = list(map(int, input().split(':')))
    time.reverse()
    print(*timetobin(time))