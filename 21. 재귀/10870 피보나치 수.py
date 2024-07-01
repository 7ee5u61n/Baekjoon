def fibonacci(N):
    if N < 2:
        return N
    else:
        return (fibonacci(N-2)+fibonacci(N-1))

print(fibonacci(int(input())))