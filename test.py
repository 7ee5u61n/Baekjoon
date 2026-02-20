chess = {'K': 0, 'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9,
         'k': 0, 'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, '.': 0}

white = 0
black = 0
for i in range(8):
    row = str(input())
    for piece in row:
        if piece.isupper():
            white += chess[piece]
        else:
            black += chess[piece]

print(white - black)