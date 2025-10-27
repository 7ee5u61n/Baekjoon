type = {'in-out': ['fdsajkl;', 'jkl;fdsa'], 'out-in': ['asdf;lkj', ';lkjasdf'],
        'stairs': ['asdfjkl;'], 'reverse': [';lkjfdsa']}

s = str(input())

for k, v in type.items():
    if s in v:
        print(k)
        exit()

print('molu')