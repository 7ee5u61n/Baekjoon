h, m = map(int, input().split())
cookingTime = int(input())

newH = h + (m + cookingTime) // 60
newM = (m + cookingTime) % 60

if newH >= 24:
    newH -= 24

print(newH, newM)