T = int(input())
for _ in range(T):
    n = int(input())
    candidate = list(int(input()) for _ in range(n))
    maxVote = max(candidate)

    if candidate.count(maxVote) > 1:
        print('no winner')
    else:
        winner = candidate.index(maxVote) + 1
        if maxVote > sum(candidate) / 2:
            print(f'majority winner {winner}')
        else:
            print(f'minority winner {winner}')