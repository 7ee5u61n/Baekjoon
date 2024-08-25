science = []
social = []

for _ in range(4):
    science.append(int(input()))
for _ in range(2):
    social.append(int(input()))

science.sort()
social.sort()

science.remove(science[0])
social.remove(social[0])

print(sum(science) + sum(social))