agent = []
for i in range(1, 6):
    name = str(input())
    for j in range(len(name)-2):
        if name[j:j+3] == 'FBI':
            agent.append(i)
            break
if agent:
    print(*agent)
else:
    print("HE GOT AWAY!")