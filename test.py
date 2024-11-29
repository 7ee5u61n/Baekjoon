import math

n = int(input())
fileSizes = list(map(int, input().split()))
cluster = int(input())

disk = 0

for file in fileSizes:
    disk += cluster*(math.ceil(file/cluster))
    
print(disk)