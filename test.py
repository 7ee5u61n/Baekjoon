n = int(input())
if n >= 1000000:
    print(int(n*0.20), int(n*0.80))
elif n >= 500000:
    print(int(n*0.15), int(n*0.85))
elif n >= 100000:
    print(int(n*0.10), int(n*0.90))
else:
    print(int(n*0.05), int(n*0.95))
