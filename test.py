n = str(input())

number = [0, 1, 2, 3, 5, 6, 7, 8, 9]

dec = 0
for i in range(len(n)):
    if int(n[i]) > 4:
        dec += (int(n[i])-1)*(9**(len(n)-i-1))
    else:
        dec += int(n[i])*(9**(len(n)-i-1))

print(dec)