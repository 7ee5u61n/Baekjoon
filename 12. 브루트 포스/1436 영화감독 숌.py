#666, 1666, 2666, 3666, 4666,5666,6660,6666,6667,6668,6669,7666,8666,9666,10666,11
N = int(input())
terminator = 666
count = 0

while N:
    if '666' in str(terminator): # 666 있는지 확인
        count += 1
    if count == N:
        print(terminator)
        break
    terminator += 1 # 없으면 1씩 증가