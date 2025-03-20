dart = list(map(int, input().split()))

alice = (dart[(dart.index(20)-1)%20]+20+dart[(dart.index(20)+1)%20])/3
bob = (sum(dart)/len(dart))

if alice > bob:
    print('Alice')
elif alice < bob:
    print('Bob')
else:
    print('Tie')