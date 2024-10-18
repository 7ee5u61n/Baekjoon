print('재료 개수')
n = int(input())

numerator = 0
denominator = 0
for i in range(n):
    print('용량, 도수')
    a, b = map(int, input().split())
    numerator += (a*b)
    denominator += a

volume = round(numerator/denominator, 1)
alcohol = round(volume*0.01*denominator*0.785)

print('도수: %, 알코올량: g')
print(volume, alcohol)