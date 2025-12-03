question = {'animal': 'Panthera tigris', 'tree': 'Pinus densiflora', 'flower': 'Forsythia koreana'}
while True:
    s = str(input())
    if s == 'end':
        break
    else:
        print(question[s])
