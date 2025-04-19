keypad = [[''], ['a', 'b', 'c'], ['d', 'e', 'f'],
          ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
          ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

arr = list(map(int, input().split()))
s = str(input())

key = [[] for _ in range(9)]
for i in range(9):
    key[i] = keypad[arr[i]-1]

output = '#'
for i in range(len(s)):
    for j in range(9):
        if s[i] in key[j]:
            temp = (str(j+1)*(key[j].index(s[i])+1))
            if output[-1] == temp[0]:
                print('#'+temp, end='')
            else:
                print(temp, end='')
            output = temp
            break