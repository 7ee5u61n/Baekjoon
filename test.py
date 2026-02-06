n = int(input())

times = set()
for i in range(2, 10):
    for j in range(1, 10):
        times.add(i)
        times.add(j)
        times.add(i * j)

if n in times:
    print(1)
else:
    print(0)