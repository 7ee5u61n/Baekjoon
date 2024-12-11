s = str(input())

sm = 0
count = 0
for i in s:
    if i == '+':
        sm += 0.5
    else:
        if i == 'A':
            sm += 4.0
            count += 1
        elif i == 'B':
            sm += 3.0
            count += 1
        elif i == 'C':
            sm += 2.0
            count += 1
        elif i == 'D':
            sm += 1.0
            count += 1
        elif i == 'F':
            count += 1

avg = sm/count
print(avg)