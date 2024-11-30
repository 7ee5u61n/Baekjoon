a, b, c, m = map(int, input().split())

figure = 0
work = 0
for i in range(24):
    # 번아웃 오면 관둬
    if figure > m:
        work = 0
        break
    else:
        # 일 할 수 있으면 해
        if figure + a <= m:
            figure += a
            work += b
        # 피곤하면 쉬어
        else:
            if figure - c >= 0:
                figure -= c
            else:
                figure = 0

print(work)