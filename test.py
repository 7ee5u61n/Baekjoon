n = int(input())
height = list(map(int, input().split()))

max_upper = 0
upper = 0
for i in range(n-1):
    if height[i] < height[i+1]:
        upper += height[i+1]-height[i]
    else:
        upper = 0
    max_upper = max(upper, max_upper)

print(max_upper)