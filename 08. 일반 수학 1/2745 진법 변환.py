# ZZZZZ 36 진법 Z = 35 35*(36^4) + 35*(36^3) ... 35*(36^0)
N, B = input().split() # B진법 수 N
N = [N]
B = int(B)
radix = 0

nList = [str(x) for x in str(N[0])] # 입력받은 문자열 한글자씩 저장

for i in range(len(nList)): # 리스트에 알파벳이 있으면 숫자로 변환
    if 65 <= ord(nList[i]) <= 90:
        nList[i] = ord(nList[i])-55

for i in range(len(nList)):
    i += 0
    base = 0
    base = int(nList[i])*(B**(len(nList)-i-1))
    radix += base

print(radix)