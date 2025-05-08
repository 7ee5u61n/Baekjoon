def match(a):
    global returnValue
    highRate = 0
    for i in range(8):
        rate = 0
        for j in range(6):
            if a[j] == letter[i][1][j]:
                rate += 1
        if rate > highRate:
            highRate = rate
            returnValue = letter[i][0]
    if highRate >= 5:
        return True
    else:
        return False

letter = [['A', '000000'], ['B', '001111'], ['C', '010011'], ['D', '011100'], 
          ['E', '100110'], ['F', '101001'], ['G', '110101'], ['H', '111010']]

n = int(input())
s = str(input())

result = ''
for i in range(n):
    a = s[i*6:(i*6)+6]
    returnValue = ''
    if match(a):
        result += returnValue
    else:
        result = i+1
        break

print(result)