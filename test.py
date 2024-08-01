T = int(input())

# 1, 246, 3971, 46, 5, 6, 7931, 8426, 91, 10
def lastData(x, y):
    patterns = {
        1: '1',
        2: '2486',
        3: '3971',
        4: '46',
        5: '5',
        6: '6',
        7: '7931',
        8: '8426',
        9: '91'
    }
    
    x = int(str(x)[-1])
    if x == 0:
        return 10
    else:
        pattern = patterns[x]
        return pattern[(y % len(pattern)) - 1]

for i in range(T):
    a, b = map(int, input().split())
    print(lastData(a, b))