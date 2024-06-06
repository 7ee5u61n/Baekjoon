numbers = []
for i in range(5):
    numbers.append(int(input()))
numbers = sorted(numbers)

avg = int(sum(numbers) / len(numbers))
mid = numbers[2]

print(avg)
print(mid)