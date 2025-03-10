n = int(input())
ace = list(map(int, input().split()))
newyork = list(map(int, input().split()))

ace_win = 0
newyork_win = 0
result = 0

for i in range(n):
    # (R, S), (S, P)
    if abs(ace[i]-newyork[i]) == 1:
        if ace[i] > newyork[i]:
            ace_win += 1
            newyork_win = 0
        else:
            ace_win = 0
            newyork_win += 1
    # (R, P)
    elif abs(ace[i]-newyork[i]) == 2:
        if ace[i] > newyork[i]:
            ace_win = 0
            newyork_win += 1
        else:
            ace_win += 1
            newyork_win = 0
    # 비김
    else:
        if ace_win > newyork_win:
            ace_win = 0
            newyork_win += 1
        else:
            ace_win += 1
            newyork_win = 0
    
    result = max(ace_win, newyork_win, result)

print(result)