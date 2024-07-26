value = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

colors = [input() for _ in range(3)]

resist = (value[colors[0]] * 10 + value[colors[1]]) * (10 ** value[colors[2]])

print(resist)