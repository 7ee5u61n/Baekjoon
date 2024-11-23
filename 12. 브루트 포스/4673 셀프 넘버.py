def self_number(x):
    if x > 10000:
        return

    sm = 0
    for i in str(x):
        sm += int(i)
    sm += x
    if sm <= 10000:
        iterator[sm] = 1
    self_number(sm)

iterator = [0]*(10001)

for i in range(1, 10001):
    if iterator[i] == 0:
        self_number(i)
    
for i in range(1, 10001):
    if iterator[i] == 0:
        print(i)