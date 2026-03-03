n = int(input())

candidate = [['PROBRAIN', 0], ['GROW', 0], ['ARGOS', 0], 
             ['ADMIN', 0], ['ANT', 0], ['MOTION', 0], 
             ['SPG', 0], ['COMON', 0], ['ALMIGHTY', 0]]

for i in range(9):
    solve = list(map(int, input().split()))
    candidate[i][1] = max(solve)

candidate.sort(key=lambda x: (-x[1]))

print(candidate[0][0])