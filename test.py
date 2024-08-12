riding = 0
most = 0
for i in range(4):
    off, on = map(int, input().split())
    riding -= off
    riding += on
    if riding > most:
        most = riding

print(most)