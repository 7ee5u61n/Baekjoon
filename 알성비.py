print('가격: 원, 용량: ml, 도수: %. 순으로 입력')
price = capacity = volume = 1
while price != 0 and capacity != 0 and volume != 0:
    price, capacity, volume = map(int, input().split())
    print(capacity*volume/price)