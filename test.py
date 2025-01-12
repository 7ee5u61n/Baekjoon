import itertools

n = int(input())
k = int(input())
card = list(str(input()) for _ in range(n))

result = set()
for i in itertools.permutations(card, k):
    result.add(''.join(i))

print(len(result))