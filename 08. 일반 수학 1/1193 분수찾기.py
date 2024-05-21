X = int(input()) # X번째 분수

i = 2 # 첫번째 분자 분모 합
sum = 1 # 분자 분모의 합
while True:
    if sum >= X:
        break
    sum = sum + i
    i = i + 1
if i % 2 == 1:
    numerator = X - sum + i -1
    denominator = sum - X + 1
    print(str(numerator) + '/' + str(denominator))
else:
    numerator = sum - X + 1
    denominator = X - sum + i -1
    print(str(numerator) + '/' + str(denominator))