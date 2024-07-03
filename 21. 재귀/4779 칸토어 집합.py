def cantoring(N):
    if N == 0:
        return '-' 
    return cantoring(N-1) + ' '*3**(N-1) + cantoring(N-1)

while True:
    try:
        print(cantoring(int(input())))
    except:
        break