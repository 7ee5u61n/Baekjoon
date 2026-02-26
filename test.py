n = int(input())
college = []
for i in range(n):
    name, year = input().split()
    college.append((name, int(year)))

college.sort(key=lambda x: -x[1])
print(college[0][0])