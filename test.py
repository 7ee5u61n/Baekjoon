N, T = map(int, input().split())

next_bus = 0
ride_bus = -1
for _ in range(N):
    S, I, C = map(int, input().split())
    
    next_bus = S
    for i in range(C):
        next_bus += I * i
        if next_bus >= T:
            ride_bus = next_bus - T
            break

print(ride_bus)