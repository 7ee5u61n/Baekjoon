# 10진법 수를 B진법으로 변환 60466175
N, B = map(int, input().split())

alphabet = list(map(chr, range(65, 91))) # 숫자를 알파벳으로 바꾸기
baseAlphabet = {}
for i in alphabet:
    baseAlphabet[alphabet.index(i) + 10] = i

radix = []
keepGoing = True

while keepGoing:
    base = N % B
    if base < 10:
        radix.append(str(base))
    else:
        radix.append(baseAlphabet[base])
    N = N // B
    if N < 1:
        keepGoing = False

radix.reverse()
print("".join(radix))