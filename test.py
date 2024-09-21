N, M = map(int, input().split())

bus_number = list(map(int, input().split()))

transfer_info = []
for _ in range(N):
    transfer_info.append(list(map(int, input().split())))

fee = 0
for i in range(M-1):
    fee += (transfer_info[bus_number[i]-1][bus_number[i+1]-1])
    
print(fee)