N = input()

count = 0
for i in range(1, len(N)):
    count += 10**(i-1)*9*i
count += (int(N)-10**(len(N)-1)+1)*len(N)
print(count)