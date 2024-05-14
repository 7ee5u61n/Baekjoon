croatian = str(input())
dic = {}

for chr in croatian:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1

print(dic)