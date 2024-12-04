direction = ['N', 'E', 'S', 'W']
di = 0
for _ in range(10):
    di = (di+int(input()))%4

print(direction[di])