m = int(input())
jSeed = int(m)
sSeed = int(m)
jStock = 0
sStock = 0

price = list(map(int, input().split()))

# 준현 매매법
for i in range(14):
    if jSeed // price[i] > 0:
        jStock += jSeed // price[i]
        jSeed -= (jSeed // price[i]) * price[i]
# 남은거
if jStock:
    jSeed += jStock * price[13]
    jStock = 0

# 성민 매매법
for i in range(3, 14):
    # 3일 연속 증가
    if sStock and price[i-3] < price[i-2] < price[i-1] < price[i]:
        sSeed += sStock * price[i]
        sStock = 0
    # 3일 연속 감소
    if price[i-3] > price[i-2] > price[i-1] > price[i]:
        if sSeed // price[i] > 0:
            sStock += sSeed // price[i]
            sSeed -= (sSeed // price[i]) * price[i]
# 남은거        
if sStock:
    sSeed += sStock * price[13]
    sStock = 0

if jSeed > sSeed:
    print('BNP')
elif jSeed < sSeed:
    print('TIMING')
else:
    print('SAMESAME')