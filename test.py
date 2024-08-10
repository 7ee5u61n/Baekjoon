N = int(input())
pick1 = int(input())
vote = [0]

for i in range(N-1):
    vote.append(int(input()))
vote.sort(reverse=True)

bride = 0
while True:
    if N == 1:
        print(0)
        break
    if vote[0] >= pick1:
        pick1 += 1
        vote[0] -= 1
        bride += 1
        vote.sort(reverse=True)
    else:
        print(bride)
        break