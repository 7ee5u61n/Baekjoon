import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    a, b = map(int, input().split())
    for _ in range(n):
        ui, vi = map(int, input().split())
    
    print(f'Material Management {test_case}')
    print('Classification ---- End!')