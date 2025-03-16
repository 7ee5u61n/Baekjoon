n1, n2 = map(int, input().split())
group1 = list(input())
group2 = list(input())
t = int(input())

group1.reverse()
sequence = group1 + group2

for _ in range(t):
    for i in range(len(sequence)-1):
        if sequence[i] in group1 and sequence[i+1] in group2:
            sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
            
            if sequence[i+1] == group1[-1]:
                break

for i in range(n1+n2):
    print(sequence[i], end='')