n = int(input())

for test_case in range(1, n+1):
    a = str(input())
    b = str(input())
    
    alphabet = [0]*26
    for i in a:
        alphabet[ord(i)-97] += 1
    for i in b:
        alphabet[ord(i)-97] -= 1

    result = 0
    for i in range(26):
        result += abs(alphabet[i])

    print(f'Case #{test_case}: {result}')
    