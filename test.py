def quest(level, data):
    result = []
    for lv1, lv2, lv3 in data:
        if level < lv1:
            result.append(0)
        elif level >= lv3:
            result.append(100)
        elif level >= lv2:
            result.append(300)
        else:
            result.append(500)
    return result

arcane = [[200, 210, 220], [210, 220, 225], [220, 225, 230], [225, 230, 235], [230, 235, 245], [235, 245, 250]]
authentic = [[260, 265, 270], [265, 270, 275], [270, 275, 280], [275, 280, 285], [280, 285, 290], [285, 290, 295], [290, 295, 300]]

n = int(input())

print(*quest(n, arcane))
print(*quest(n, authentic))