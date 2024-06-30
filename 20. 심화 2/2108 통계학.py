import sys
from collections import Counter

N = int(sys.stdin.readline())

integers = []
for i in range(N):
    integers.append(int(sys.stdin.readline()))

def avg(x):
    avg = round(sum(x) / len(x))
    return avg

def med(x):
    x = sorted(x)
    med = x[len(x)//2]
    return med

def mod(x):
    x = sorted(x)
    mod = Counter(x).most_common(2)
    
    if len(x) > 1 and mod[0][1] == mod[1][1]:
        return mod[1][0]
    else:
        return mod[0][0]
    
def ran(x):
    ran = max(x) - min(x)
    return ran

print(avg(integers))
print(med(integers))
print(mod(integers))
print(ran(integers))