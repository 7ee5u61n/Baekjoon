dynamic_count = 0
def dynamic_fibonacci(n):
    global dynamic_count
    f = [1, 1]
    for i in range(2, n):
        dynamic_count += 1
        f.append(f[i-1] + f[i-2])
    return f[n-1]

n = int(input())
recursion_count = dynamic_fibonacci(n)
print(recursion_count, dynamic_count)