print('가격: 원, 용량: ml, 도수: %. 순으로 입력')
price = capacity = volume = 1
while True:
    price, capacity, volume = map(int, input().split())
    if price and capacity and volume:
        result = price / (capacity * volume)
        print(f'가격: {price}원, 용량: {capacity}ml, 도수: {volume}%, 가격/알코올: {result:.2f}원/ml')
    else:
        print('종료합니다.')
        break