import sys
N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers = sorted(numbers)
for i in range(len(numbers)):
    print(numbers[i])