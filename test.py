DNA = {'AA' : 'A', 'AG': 'C', 'AC': 'A', 'AT': 'G', 
       'GA': 'C', 'GG': 'G', 'GC': 'T', 'GT': 'A',
       'CA': 'A', 'CG': 'T', 'CC': 'C', 'CT': 'G',
       'TA': 'G', 'TG': 'A', 'TC': 'G', 'TT': 'T'}

N = int(input())
A = list(input())

for i in range(N-1):
    S = A.pop(-2) + A.pop(-1)
    if S in DNA:
        A.append(DNA.get(S))
print(*A)