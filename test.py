ABC = list(map(int, input().split()))

ABC.pop(ABC.index(max(ABC)))
print(max(ABC))