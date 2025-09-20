s = str(input())

result = len(s) + s.count(':') + s.count('_')*5

print(result)