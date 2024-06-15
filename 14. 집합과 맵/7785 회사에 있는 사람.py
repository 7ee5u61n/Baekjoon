n = int(input()) # 출입 기록 수

inCompany = set()
for i in range(n):
    name, state = input().split()
    if state == 'enter':
        inCompany.add(name)
    else:
        inCompany.remove(name)

inCompany = list(inCompany)
inCompany.sort(reverse=True)

for i in range(len(inCompany)):
    print(inCompany[i])