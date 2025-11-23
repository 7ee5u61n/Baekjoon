T = int(input())

for _ in range(T):
    n = str(input())
    if (int(n)+1) % int(n[2:]):
        print('Bye')
    else:
        print('Good')