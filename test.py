dwarf = [int(input()) for _ in range(9)]
dwarf.sort()
rest = sum(dwarf)-100

for i in range(9):
    if len(dwarf) == 9:
        for j in range(i, 9):
            if dwarf[i]+dwarf[j] == rest:
                dwarf.pop(i)
                dwarf.pop(j-1)
                break
    
for i in range(7):
    print(dwarf[i])