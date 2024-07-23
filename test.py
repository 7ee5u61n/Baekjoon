N = int(input())

seat = dict.fromkeys(range(1, 101), 0)
people = list(map(int, input().split()))

for i in range(len(people)):
    seat[people[i]] += 1

count = 0
for i in range(len(seat)):
    if seat[i+1] > 1:
        count += seat[i+1] -1

print(count)